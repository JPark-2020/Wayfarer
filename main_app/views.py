from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.views.generic.base import TemplateView 
from django.views import View
from .models import Profile, Location, Post  
from django.contrib.auth.forms import UserCreationForm 
from .forms import ProfileUpdate, PostCreate  

class Home(TemplateView):
    template_name = "home.html"


class ProfilePage(View):
    def get(self, request):
        current_user = request.user
        user_profile = Profile.objects.get(user_id = current_user)
        form = ProfileUpdate() 
        context = {"user_profile": user_profile, "form": form}
        return render(request, "profile.html", context)

    def post(self, request):
        current_user = request.user
        user_profile = Profile.objects.get(user_id = current_user)
        form = ProfileUpdate() 
        context = {"user_profile": user_profile, "form": form}
        if request.method == "POST":
            form = ProfileUpdate(request.POST, instance=user_profile) 
            if form.is_valid():
                form.save() 
        return render(request, "profile.html", context)

class SignUp(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('/portfolio')
        else:
            return redirect("/")

class LocationList(View):
    def get(self, request):
        all_locations = Location.objects.all()
        context = {"all_locations":all_locations}
        return render(request, "location-list.html", context)

class LocationDetail(View):
    def get(self, request, locationname):
        found_location = Location.objects.get(name = locationname)
        context = {"found_location": found_location}
        return render(request, 'location-detail.html', context)

    # def post(self, request):
    #     current_user = request.user 

        
