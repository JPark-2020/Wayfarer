from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.views.generic.base import TemplateView 
from django.views import View
from .models import Profile, Location, Post  
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login
from .forms import ProfileUpdate, PostCreate
from django.http import HttpResponseRedirect


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
    
class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect("profile_page")
        else:
            return redirect("signup_page")

class LocationList(View):
    def get(self, request):
        all_locations = Location.objects.all()
        context = {"all_locations":all_locations}
        return render(request, "location-list.html", context)

class LocationDetail(View):
    def get(self, request, locationname): 
        form = PostCreate()
        found_location = Location.objects.get(name = locationname)
        location_posts = Post.objects.filter(post_location_id = found_location.id)
        context = {"found_location": found_location, "form": form, "location_posts":location_posts}
        return render(request, 'location-detail.html', context)

    def post(self, request, locationname):
        form = PostCreate(request.POST)
        current_user = request.user
        found_location = Location.objects.get(name = locationname)

        if form.is_valid():
            
            form = form.save(commit=False)
            form.post_location = Location.objects.get(id = found_location.id)
            form.author = Profile.objects.get(user_id = current_user)
            form.save()

        return HttpResponseRedirect(self.request.path_info)
                

class PostList(View):
    def get(self, request):
        all_posts = Post.objects.all()
        context = {"all_posts": all_posts}
        return render(request, "post-list.html", context)



        
