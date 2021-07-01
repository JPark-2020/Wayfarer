from django.forms import ModelForm 
from .models import Profile, Post  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 

class ProfileUpdate(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_location', 'image']

class PostCreate(ModelForm):
    class Meta:
        model = Post 
        fields = ['title', 'content']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.TextInput()
    last_name= forms.TextInput()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
