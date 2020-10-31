from django.db import models
from django.conf import settings

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class Images(models.Model):

    post = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    #def __init__(self, username):
        #self.username = username


    #def __str__(self):
     #   return self.username
      #  return self.post.title + "Image"


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
