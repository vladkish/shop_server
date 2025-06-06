from django.urls import path
from .views import basket_view, basket, add_basket, minus_basket

app_name = "products"

urlpatterns = [
    path('basket/', basket_view, name="basket_view"),
    path('add/basket/<int:product_id>/', basket, name="basket"),
    
    # Fnc add and minus qantity basket.
    path('plus/basket/<int:basket_id>/', add_basket, name="add_basket"), 
    path('minus/basket/<int:basket_id>/', minus_basket, name="minus_basket")
]
