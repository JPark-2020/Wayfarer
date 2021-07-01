from django.forms import ModelForm 
from .models import Profile, Post  

class ProfileUpdate(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_location', 'image']

class PostCreate(ModelForm):
    class Meta:
        model = Post 
        fields = ['title', 'content']


