# Generated by Django 4.1 on 2023-01-11 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('ticker', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('company_name', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
                ('current_price', models.FloatField()),
                ('market_cap', models.FloatField()),
                ('enterprise_value', models.FloatField()),
                ('forward_pe', models.FloatField()),
                ('price_to_sales', models.FloatField()),
                ('price_to_book', models.FloatField()),
                ('enterprise_to_rev', models.FloatField()),
                ('enterprise_to_ebitda', models.FloatField()),
                ('profit_margins', models.FloatField()),
                ('roa', models.FloatField()),
                ('roe', models.FloatField()),
                ('leverage', models.FloatField()),
                ('beta', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RelativeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.SlugField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('stocks', models.ManyToManyField(blank=True, related_name='relative_tables', to='relative_table_api.stock')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-edited'],
            },
        ),
    ]
