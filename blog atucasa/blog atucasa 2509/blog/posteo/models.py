from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

class User(AbstractUser):
    pass
    def __str__(self):
        return self.username

# Create your models here.

class Posteo(models.Model):
    title = models.CharField(max_length=100),
    content = models.TextField(),
    thumbnail = models.ImageField(),
    publish_date = models.DateTimeField(auto_now_add=True),
    last_updated = models.DateTimeField(auto_now=True),
    autor = models.ForeignKey(User, on_delete=models.CASCADE),
    #slug = models.SlugField(defould='')
    #models.IntegerField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    
    @property
    def get_Comment_count(self):
       return self.Comment_set.all().count()
    @property
    def get_view_count(self):
        return self.posteoview_set.all().count()
    @property
    def get_like_count(self):
        return self.like_set.all().count()
    @property
    def get_dislike_count(self):
        return self.dislike_set.all().count()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Posteo = models.ForeignKey(Posteo, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class posteoView(models.Model):
    models.ForeignKey(User, on_delete=models.CASCADE)
    Posteo = models.ForeignKey(Posteo, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.user.username

class Like(models.Model):
    models.ForeignKey(User, on_delete=models.CASCADE)
    posteo = models.ForeignKey(Posteo, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Dislike(models.Model):
    models.ForeignKey(User, on_delete=models.CASCADE)
    posteo = models.ForeignKey(Posteo, on_delete=models.CASCADE)

