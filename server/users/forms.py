from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User

class LoginForm(AuthenticationForm):
    pass

class SignForm(UserCreationForm):
    
    email = forms.CharField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')