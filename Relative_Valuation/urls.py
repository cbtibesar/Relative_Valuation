from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('users.urls', namespace='users')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/stock_api/', include('relative_table_api.urls', namespace='relative_table'))
]
