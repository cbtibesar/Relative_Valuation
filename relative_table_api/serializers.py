from rest_framework import serializers
from .models import RelativeTable
from users.models import User
from django.conf import settings

class RelativeTableSerializer(serializers.ModelSerializer):
    stocks = StockSerializer(many=True, required=False)
    class Meta:
        model = RelativeTable
        fields = ['url', 'title', 'stocks', 'created', 'edited']
        extra_kwargs = {'stocks': {'required': False}, 'url':{'required':False}}
