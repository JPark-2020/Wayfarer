from django.forms import ModelForm 
from .models import Profile 


class ProfileUpdate(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_location', 'image']

        