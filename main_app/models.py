from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField 




#One user has one profile. One profile has one user. 
class Profile(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(min_length = 1, max_length= 30)
    profile_location = models.CharField(max_length = 80, blank=True, null=True)
    join_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to="images", default="settings.MEDIA_ROOT/images/nolocation.png")

    def __str__(self):
        return self.name 

#One post has one author, one author has many posts 

class Post(Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(min_length = 3, max_length = 30)
    content = models.CharField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.title}'

#one post to one location. One location can have many posts 
class Location(Model):
    name = models.CharField(max_length = 100)
    image = models.FileField(upload_to="images", default="settings.MEDIA_ROOT/images/noprofile.png")
    posts = models.ForeignKey(Post, null=True, blank=True, related_name="post_location") 

    def __str__(self):
        return self.name 

