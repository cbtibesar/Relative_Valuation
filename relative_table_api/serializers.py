from rest_framework import serializers
from .models import Stock, RelativeTable
from users.models import User
from django.conf import settings

class StockSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(max_length=50, required=False)
    sector = serializers.CharField(max_length=50, required=False)
    current_price = serializers.FloatField(required=False)
    market_cap = serializers.FloatField(required=False)
    enterprise_value = serializers.FloatField(required=False)
    forward_pe = serializers.FloatField(required=False)
    enterprise_to_rev = serializers.FloatField(required=False)
    enterprise_to_ebitda = serializers.FloatField(required=False)
    profit_margins = serializers.FloatField(required=False)
    roe = serializers.FloatField(required=False)
    roa = serializers.FloatField(required=False)
    leverage = serializers.FloatField(required=False)
    price_to_book = serializers.FloatField(required=False)
    beta = serializers.FloatField(required=False)
    price_to_sales = serializers.FloatField(required=False)
    class Meta:
        model = Stock
        fields = ['ticker', 'company_name','sector', 'current_price', 'market_cap', 'enterprise_value', 'forward_pe', 'price_to_book', 'price_to_sales',
                    'enterprise_to_rev', 'enterprise_to_ebitda', 'profit_margins', 'roe', 'roa', 'leverage', 'beta']
        extra_kwargs = {'relative_tables': {'required': False}}

class RelativeTableSerializer(serializers.ModelSerializer):
    stocks = StockSerializer(many=True, required=False)
    class Meta:
        model = RelativeTable
        fields = ['url', 'title', 'stocks', 'created', 'edited']
        extra_kwargs = {'stocks': {'required': False}, 'url':{'required':False}}
