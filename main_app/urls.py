from . import views 
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name="home_page"),
    path('profile/', views.ProfilePage.as_view(), name="profile_page"),
    path('accounts/signup', views.SignUp.as_view(), name="signup_page"),
]
