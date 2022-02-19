from django.db import models
from django.utils import timezone
from django.conf import settings
from django.template.defaultfilters import slugify
from stock_api.models import Stock



class RelativeTable(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stocks = models.ManyToManyField(Stock, related_name="relative_tables", blank=True)
    url = models.SlugField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-edited',]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.url = slugify(self.user.username) + '-' + slugify(self.title)
        super().save(*args, **kwargs)

