from django import forms
from django.contrib.auth.forms import UserChangeForm
from users.models import User

# Change User.
class ChangeForm(UserChangeForm):
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={ 
        "readonly": True
    }))
    
    image = forms.ImageField(widget=forms.FileInput(attrs={
        "class" : "select_img", "placeholder" : "Выберете изображение"
    }), required=False)
        
    class Meta:
        model = User
        fields = ('username', 'email', 'image')