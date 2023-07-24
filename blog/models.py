from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# class Author(models.Model):
#     username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     date_of_birth = models.DateField(blank=True, null=True)
#     photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

#     def __str__(self):
#         return f'Профиль {self.user.username})'

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    profile_pic = models.ImageField(upload_to='', blank=True, default='static/media/def.png')
    
    def __str__(self):
        return f'@{self.user} | {self.name}'
    

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # image = models.ImageField(upload_to='', blank=True)
    published_date = models.DateTimeField(blank=True, null=True)
    count_of_view = models.IntegerField(null=True, blank=True, default=0)
    likes_check = models.ManyToManyField(User, related_name='likes', blank=True)
    likes = models.IntegerField(null=True, blank=True, default=0)
    # dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    # image = models.ImageField(upload_to='', blank=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE,)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.author.username} | {self.post.title}'