
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('PizzaDelivery.authentication.urls')),
    path('orders/', include('PizzaDelivery.orders.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
