from .models import RelativeTable
from .serializers import StockSerializer, RelativeTableSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
import yfinance as yf
import json
from django.shortcuts import get_object_or_404
from django.core import serializers
from datetime import datetime, timezone, timedelta


class RelativeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = RelativeTable.objects.all()
    serializer_class = RelativeTableSerializer

    def get_object(self, queryset=None, **kwargs):
            url = self.kwargs.get('pk')
            return get_object_or_404(RelativeTable, url=url)

    def patch(self, request, pk, *args, **kwargs):
        relative_table = RelativeTable.objects.get(url=pk)
        tickers = self.request.data.get('stocks')
        title = self.request.data.get('title')
        response_data = []
        if title is not None:
            RelativeTable.objects.filter(url=pk).update(title=title)
        if tickers is not None:
            for ticker in tickers:
                ticker = ticker.upper()
                if not Stock.objects.filter(ticker=ticker).exists():
                    stock_data = create_stock(ticker)
                    stock_serializer = StockSerializer(data=stock_data)
                    stock_serializer.is_valid(raise_exception=True)
                    stock_serializer.save()
                    response_data.append(stock_data)
                elif(datetime.now(timezone.utc) - Stock.objects.get(ticker=ticker).edited > timedelta(seconds=24)):
                    stock_data = create_stock(ticker)
                    stock = Stock.objects.get(ticker=ticker)
                    stock_serializer = StockSerializer(stock, data=stock_data, partial=True)
                    stock_serializer.is_valid(raise_exception=True)
                    stock_serializer.save()
                stock = Stock.objects.get(ticker=ticker)
                relative_table.stocks.add(stock)
                relative_table.save()

        serializer = RelativeTableSerializer(relative_table)
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

    def put(self, request, pk, *args, **kwargs):
        relative_table = RelativeTable.objects.get(url=pk)
        tickers = self.request.data.get('stocks_to_remove')
        if tickers is not None:
            for ticker in tickers:
                if Stock.objects.filter(ticker=ticker).exists():
                    stock = Stock.objects.get(ticker=ticker)
                    relative_table.stocks.remove(stock)

        serializer = RelativeTableSerializer(relative_table)
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)


class RelativeList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = RelativeTableSerializer
    def perform_create(self, serializer):
        user = self.request.user
        if serializer.is_valid():
            serializer.save(user=user)

    def get_queryset(self):
        user=self.request.user
        return RelativeTable.objects.filter(user=user)







