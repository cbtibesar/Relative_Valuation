from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length=5, unique=True, primary_key=True)
    start_date = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(auto_now=True)
    company_name = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    current_price = models.FloatField()
    market_cap = models.FloatField()
    enterprise_value = models.FloatField()
    forward_pe = models.FloatField()
    price_to_sales = models.FloatField()
    price_to_book = models.FloatField()
    enterprise_to_rev = models.FloatField()
    enterprise_to_ebitda = models.FloatField()
    profit_margins = models.FloatField()
    roa = models.FloatField()
    roe = models.FloatField()
    leverage = models.FloatField()
    beta = models.FloatField()


    def __str__(self):
        return self.ticker
