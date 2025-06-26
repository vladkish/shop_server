from django.urls import path
from .views import basket_view, basket, add_basket, minus_basket, delete_basket, delete_all_baskets, index

app_name = "products"

urlpatterns = [
    path('basket/', basket_view, name="basket_view"),
    path('add/basket/<int:product_id>/', basket, name="basket"),
    
    # Fnc add and minus qantity basket.
    path('plus/basket/<int:basket_id>/', add_basket, name="add_basket"), 
    path('minus/basket/<int:basket_id>/', minus_basket, name="minus_basket"),
    
    # Delete basket.
    path('delete/basket/<int:basket_id>/', delete_basket, name="delete_basket"),
    path('delete/all/basket/', delete_all_baskets, name="delete_baskets"),

    # Filter urls.
    path('category/<int:category_id>/', index, name="category")
]
