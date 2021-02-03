from django.db import models
from django.contrib.auth.models import User

class UserModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)
    website_link = models.URLField(blank=True)



# Create your models here.
