from django.db import models
from django.contrib.auth.models import User





# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    

def __str__(self):
    return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=100)
    

def __str__(self):
    return self.name