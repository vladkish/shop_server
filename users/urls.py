from django.urls import path
from .views import login, sign

app_name = 'users'

urlpatterns = [
    path('login/', login, name="login"),
    path('sign/', sign, name="sign")
]
