from .models import Stock, RelativeTable
from .serializers import StockSerializer, RelativeTableSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
import yfinance as yf
import json


class RelativeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RelativeTable.objects.all()
    serializer_class = RelativeTableSerializer

    def update(self, request, pk, *args, **kwargs):
        relative_table = RelativeTable.objects.get(id=pk)

        tickers = self.request.data.get('stocks')
        title = self.request.data.get('title')

        if title is not None:
            RelativeTable.objects.filter(id=pk).update(title=title)
        if tickers is not None:
            for ticker in tickers:
                ticker = ticker.upper()
                stock = Stock.objects.get(ticker=ticker)
                relative_table = RelativeTable.objects.get(id=pk)
                relative_table.stocks.add(stock)
                relative_table.save()


        return Response("Updated successfully", status=204)


class RelativeList(generics.ListCreateAPIView):
    queryset = RelativeTable.objects.all()
    serializer_class = RelativeTableSerializer
    def perform_create(self, serializer):
        user = self.request.user
        if serializer.is_valid():
            serializer.save(user=user)


class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def create(self, request, *args, **kwargs):
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

        ticker = self.request.data.get('ticker')
        table = self.request.data.get('table')
        info = yf.Ticker(ticker).info

        stock_data = {
            'ticker': ticker.upper(),
            'company_name': check_for_null_string(info, "shortName"),
            'sector': check_for_null_string(info, "sector"),
            'market_cap': check_for_null_int(info, "marketCap"),
            'current_price': check_for_null_int(info, "currentPrice"),
            'enterprise_value': check_for_null_int(info, "enterpriseValue"),
            'forward_pe': check_for_null_int(info, "forwardPE"),
            'enterprise_to_rev': check_for_null_int(info, "enterpriseToRevenue"),
            'enterprise_to_ebitda': check_for_null_int(info, "enterpriseToEbitda"),
            'profit_margins': check_for_null_int(info, "profitMargins"),
            'roe': check_for_null_int(info, "returnOnEquity"),
            'table': table
        }

        serializer = self.get_serializer(data=stock_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()


class StockDetail(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
