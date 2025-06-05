from django.shortcuts import render
from .models import Product, Category

def index(request):
    
    context = {
        "products" : Product.objects.all(),
        "categoryies" : Category.objects.all()
    }
    
    return render(request, 'products/product.html', context)