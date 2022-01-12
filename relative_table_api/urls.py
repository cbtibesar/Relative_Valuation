from django.urls import path, include
from .views import StockList, StockDetail, RelativeList, RelativeDetail

app_name = 'relative_valuation'

urlpatterns = [
    path('', StockList.as_view(), name='stock_list'),
    path('relative_table/', RelativeList.as_view(), name='relative_list'),
    path('relative_table/<str:pk>/', RelativeDetail.as_view(), name='relative_detail'),
    path('stock/<str:pk>/', StockDetail.as_view(), name='stock')
]
