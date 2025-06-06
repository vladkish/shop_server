from django.shortcuts import render, redirect
from .models import Product, Category, Basket
from django.contrib.auth.decorators import login_required

def index(request):
    
    context = {
        "products" : Product.objects.all(),
        "categoryies" : Category.objects.all()
    }
    
    return render(request, 'products/product.html', context)

@login_required
def basket_view(request):
    context = {
        'baskets' : Basket.objects.filter(user=request.user)
    }
    return render(request, 'products/basket.html', context)

# Logic basket.
def basket(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    
    if baskets.exists():
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    else:
        Basket.objects.create(user=request.user, product=product, quantity=1)
    
    return redirect(request.META["HTTP_REFERER"])