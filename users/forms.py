from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.models import User
class CustomUserCreationForm(UserCreationForm):
    address = forms.CharField(max_length=30)
    class Meta:
        model = CustomUser
        fields = ('username', 'email','address','password1','password2')

class CustomUserChangeForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    address = forms.CharField(max_length=30)
    class Meta:
        model = CustomUser
        fields = ('username', 'email','address')
        