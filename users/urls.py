from django.urls import path
from .views import login, sign, user_logout, delete_user

app_name = 'users'

urlpatterns = [
    path('login/', login, name="login"),
    path('sign/', sign, name="sign"),
    path('logout/', user_logout, name="user_logout"),
    path('delete/user/', delete_user, name="delete_user")
]
