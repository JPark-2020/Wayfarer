from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User



class Location(Model):
    name = models.CharField(max_length = 100)
    state = models.CharField(max_length=4)
    image = models.CharField(max_length=1000, default="https://www.pngarea.com/pngm/0/4941568_location-icon-png-location-logo-png-hd-hd.png")

    def __str__(self):
        return f'{self.name}, {self.state}' 

    class Meta:
        ordering = ['state']

#One user has one profile. One profile has one user. 
class Profile(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 30)
    profile_location = models.CharField(max_length = 80, blank=True, null=True)
    join_date = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=1000, default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png")

    def __str__(self):
        return self.name 

#One post has one author, one author has many posts 

class Post(Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length = 30)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    post_location = models.ForeignKey(Location, on_delete = models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'{self.author} - {self.title}'

