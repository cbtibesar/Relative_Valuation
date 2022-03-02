from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length=5, unique=True, primary_key=True)
    start_date = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(auto_now=True)

    company_name = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    current_price = models.FloatField()
    percent_change = models.FloatField()

    market_cap = models.FloatField()
    enterprise_value = models.FloatField()

    forward_pe = models.FloatField()
    price_sales = models.FloatField()
    price_book = models.FloatField()
    price_FCF = models.FloatField()
    debt_equity = models.FloatField()
    eps = models.FloatField()
    eps_future_5 = models.FloatField() 

    enterprise_to_rev = models.FloatField()
    enterprise_to_ebitda = models.FloatField()

    profit_margins = models.FloatField()
    gross_margins = models.FloatField()

    roa = models.FloatField()
    roe = models.FloatField()
    roi = models.FloatField()

    beta = models.FloatField()

    relative_strength = models.FloatField()
    analyst_recom = models.FloatField()
    analyst_target = models.FloatField()
    upside = models.FloatField()

    SMA200 = models.FloatField()
    SMA20 = models.FloatField()



    def __str__(self):
        return self.ticker
