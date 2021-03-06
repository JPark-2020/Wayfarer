from . import views 
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name="home_page"),
    path('profile/', views.ProfilePage.as_view(), name="profile_page"),
    path('accounts/signup', views.Signup.as_view(), name="signup_page"),
    path('locations/', views.LocationList.as_view(), name="location_list_page"), 
    path('locations/<str:locationname>', views.LocationDetail.as_view(), name="location_detail_page"),
    path('posts/', views.PostList.as_view(), name="post_list_page"),
    path('search-locations/', views.SearchLocations, name='search_locations'),
]
