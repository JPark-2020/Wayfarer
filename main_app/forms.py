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


# class Post(Model):
#     author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
#     title = models.CharField(max_length = 30)
#     content = models.CharField(max_length=300)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.author} - {self.title}'
