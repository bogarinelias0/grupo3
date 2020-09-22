from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
    def __str__(self):
        return self.username

# Create your models here.

class posteo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbmail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Coment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posteo = models.ForeignKey(posteo, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class posteoview(models.Model):
    models.ForeignKey(User, on_delete=models.CASCADE)
    posteo = models.ForeignKey(posteo, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.user.username

class like(models.Model):
    models.ForeignKey(User, on_delete=models.CASCADE)
    posteo = models.ForeignKey(posteo, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class dislike(models.Model):
    models.ForeignKey(User, on_delete=models.CASCADE)
    posteo = models.ForeignKey(posteo, on_delete=models.CASCADE)

