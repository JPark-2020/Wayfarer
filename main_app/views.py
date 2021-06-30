from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.views.generic.base import TemplateView 
from django.views import View
from .models import Profile, Location, Post  
from django.contrib.auth.forms import UserCreationForm 

class Home(TemplateView):
    template_name = "home.html"


class ProfilePage(View):
    def get(self, request):
        current_user = request.user
        user_profile = Profile.objects.get(user_id = current_user)
        context = {"user_profile": user_profile}
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
