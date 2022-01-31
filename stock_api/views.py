from .models import Stock
from .serializers import StockSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
import yfinance as yf
import json
from django.shortcuts import get_object_or_404
from django.core import serializers

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

