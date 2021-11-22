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
    # relative_tables = RelativeTableSerializer(many=True, read_only=True)

    class Meta:
        model = Stock
        fields = ['ticker', 'company_name','sector', 'current_price', 'market_cap', 'enterprise_value', 'forward_pe', 'enterprise_to_rev', 'enterprise_to_ebitda', 'profit_margins', 'roe']
        extra_kwargs = {'relative_tables': {'required': False}}

    # def create(self, validated_data):
    #     return Stock.objects.create(**validated_data)


class RelativeTableSerializer(serializers.ModelSerializer):
    stocks = StockSerializer(many=True)
    class Meta:
        model = RelativeTable
        fields = ['id', 'title', 'stocks']
        extra_kwargs = {'stocks': {'required': False}}

