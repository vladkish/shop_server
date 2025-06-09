from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User

# Import Form.
from .forms import LoginForm, SignForm

def login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, password=password, username=username)
            
            if user:
                auth.login(request, user)
                
                messages.success(request, 'Вошли!')
                return redirect('index')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    context = {
        'form' : form
    }
    
    return render(request, 'users/login.html', context)

def sign(request):
    if request.method == "POST":
        form = SignForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            
            messages.success(request, 'Создали')
            return redirect('index')
    else:
        form = SignForm()
    context = {
        'form' : form
    }
    return render(request, 'users/sign.html', context)

@login_required
def user_logout(request):
    auth.logout(request)
    return redirect(request.META['HTTP_REFERER'])

@login_required
def delete_user(request):
    user = User.objects.filter(username=request.user.username).first().delete()
    return redirect('index')