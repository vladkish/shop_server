from django.shortcuts import render, redirect, HttpResponse
from .models import Product, Category, Basket
from django.contrib.auth.decorators import login_required
from .forms import ChangeForm
from django.contrib import messages
from django.shortcuts import get_object_or_404

def index(request, category_id=None):
    context = {
        # Правильно решение фильтрации по категориям на сайте.
        "products" : Product.objects.filter(category_id=category_id) if category_id else Product.objects.all(),
        "categoryies" : Category.objects.all(),
    }
    
    try:
        if Basket.objects.filter(user=request.user).count() >= 1:
            context['basket'] = 1
    except TypeError:
        pass
    
    return render(request, 'products/product.html', context)

@login_required
def basket_view(request):
    if request.method == "POST":
        form = ChangeForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Успешно изменили данные")
            return redirect("index")
        else:
            print(form.errors)
    else:
        form = ChangeForm(instance=request.user)
    context = {
        "form" : form,
        'baskets' : Basket.objects.filter(user=request.user)
    }
    return render(request, "products/basket.html", context)

# Logic basket.
@login_required
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

# Add and minus qantity basket.
@login_required
def add_basket(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.add_basket()
    
    return redirect(request.META["HTTP_REFERER"])

@login_required
def minus_basket(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    count = basket.minus_basket()
    
    if count == 0:
        Basket.objects.get(id=basket_id).delete()
    
    return redirect(request.META["HTTP_REFERER"])

@login_required
def delete_basket(request, basket_id):
    basket = Basket.objects.get(id=basket_id).delete()
    return redirect(request.META['HTTP_REFERER'])

@login_required
def delete_all_baskets(request):
    Basket.objects.filter(user=request.user).delete()
    return redirect(request.META['HTTP_REFERER'])

# Profile change.
# def change_profile(request):
#     if request.method == "POST":
#         form = UserChangeForm(data=request.POST, instance=request.user, files=request.FILES)
#         if form.is_valid():
#             form.save()
            
#             messages.success(request, "Успешно изменили данные")
#             return redirect("index")
#     else:
#         form = UserChangeForm(instance=request.user)
#     context = {
#         "form" : form,
#     }
#     return render(request, 'products/basket.html', context)