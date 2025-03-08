from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class bro(models.Model):
    title=models.CharField(max_length=100,unique=True)
    image_url=models.URLField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bro')  
