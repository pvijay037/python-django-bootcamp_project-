from django.db import models
from django.contrib.auth.models import User
from house.models import House
class Profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.FileField(upload_to ='media/user_profile',blank=True,null=True)
    house = models.ForeignKey(House,on_delete=models.CASCADE,null=True,blank=True,related_name='members')

    def __str__(self):
        return f'profile name {self.user}'



