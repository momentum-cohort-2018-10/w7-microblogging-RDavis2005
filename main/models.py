from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    users_followed = models.ManyToManyField(
        to="User", through="Following", through_fields=("following_user", "followed_user"), related_name="followers") #Who is following the user

    # def is_authenticated(self):
    #     return True

class Following(models.Model):
    following_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following_from")   #Who is doing the following
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following_to")      #Who is being followed

class Post(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts") #A post can only have one owner
    text = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments") #A post can have many comments
    text = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)