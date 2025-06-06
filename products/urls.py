from django.urls import path
from .views import basket_view, basket

app_name = "products"

urlpatterns = [
    path('basket/', basket_view, name="basket_view"),
    path('add/basket/<int:product_id>/', basket, name="basket")
]
