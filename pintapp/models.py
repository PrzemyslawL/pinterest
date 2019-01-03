from django.db import models

# Create your models here.


class MyUser(models.Model):
    email = models.EmailField(max_length=128, primary_key=True)
    nickname = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

class Photo(models.Model):
    photo = models.ImageField(max_length=255)
    description = models.TextField()
    likes = models.ManyToManyField(MyUser)

class Comment(models.Model):
    content = models.TextField()
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    my_user = models.ForeignKey(MyUser, on_delete=models.CASCADE)