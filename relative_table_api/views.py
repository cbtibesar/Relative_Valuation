from .models import Stock, RelativeTable
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

    """
    Get table objects based on the slug (url) field
    """
    def get_object(self, queryset=None, **kwargs):
            url = self.kwargs.get('pk')
            return get_object_or_404(RelativeTable, url=url)


    """
    Patch is used for adding stocks to a already created table.
    If the stock already exists, add it to the table.
    Else create the stock and add it to the table.
    """
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

    """
    Put is used for removing stocks from the table
    """
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

    """
    Get user from request when creating and listing tables
    """
    def perform_create(self, serializer):
        user = self.request.user
        if serializer.is_valid():
            serializer.save(user=user)

    def get_queryset(self):
        user=self.request.user
        return RelativeTable.objects.filter(user=user)



class StockList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def create(self, request, *args, **kwargs):
        ticker = self.request.data.get('ticker')
        table = self.request.data.get('table')
        stock_data = create_stock(ticker)

        serializer = self.get_serializer(data=stock_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()


class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

def create_stock(ticker):
    info = yf.Ticker(ticker).info
    def check_for_null_int(info, financial):
            if info[financial] is None:
                return -420.69
            else:
                return info[financial]

    def check_for_null_string(info, financial):
        if info[financial] is None:
            return "N/A"
        else:
            return info[financial]

    stock_data = {
            'ticker': ticker.upper(),
            'company_name': check_for_null_string(info, "shortName"),
            'sector': check_for_null_string(info, "sector"),
            'market_cap': check_for_null_int(info, "marketCap"),
            'current_price': check_for_null_int(info, "currentPrice"),
            'enterprise_value': check_for_null_int(info, "enterpriseValue"),
            'forward_pe': check_for_null_int(info, "forwardPE"),
            'price_to_book': check_for_null_int(info, "priceToBook"),
            'price_to_sales': check_for_null_int(info, "priceToSalesTrailing12Months"),
            'enterprise_to_rev': check_for_null_int(info, "enterpriseToRevenue"),
            'enterprise_to_ebitda': check_for_null_int(info, "enterpriseToEbitda"),
            'profit_margins': check_for_null_int(info, "profitMargins"),
            'roa': check_for_null_int(info, "returnOnAssets"),
            'roe': check_for_null_int(info, "returnOnEquity"),
            'leverage': check_for_null_int(info, "debtToEquity"),
            'beta': check_for_null_int(info, 'beta')
        }
    return stock_data




