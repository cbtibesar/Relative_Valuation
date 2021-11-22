from django.urls import path, include
from .views import StockList, StockDetail, RelativeTableViewSet
from rest_framework.routers import DefaultRouter

app_name = 'relative_valuation'


router = DefaultRouter()
router.register(r'relative_table', RelativeTableViewSet, basename='relative_table')

urlpatterns = [
    path('', StockList.as_view(), name='stock_list'),
    path(r'', include(router.urls)),
    path('stock/<str:pk>', StockDetail.as_view(), name='stock')
]
