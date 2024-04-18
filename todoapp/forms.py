from django import forms # nov 22
from django.contrib.auth.models import User #djangoile User modelinu corresponding aayitulla form aanu cheyunnathu so User model import cheyyanam
from django.contrib.auth.forms import UserCreationForm
from todoapp.models import Todos

class UserForm(UserCreationForm):#for registration
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class TodoForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=['name']
        