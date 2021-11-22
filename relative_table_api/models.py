from django.db import models
from django.utils import timezone
from django.conf import settings

class Stock(models.Model):
    ticker = models.CharField(max_length=5)
    start_date = models.DateTimeField(default=timezone.now)
    company_name = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    current_price = models.FloatField()
    market_cap = models.FloatField()
    enterprise_value = models.FloatField()
    forward_pe = models.FloatField()
    enterprise_to_rev = models.FloatField()
    enterprise_to_ebitda = models.FloatField()
    profit_margins = models.FloatField()
    roe = models.FloatField()


    def __str__(self):
        return self.ticker

class RelativeTable(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stocks = models.ManyToManyField(Stock, related_name="relative_tables", blank=True)

    def __str__(self):
        return self.title


