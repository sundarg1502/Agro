from django.db import models
import os
import datetime
from django.contrib.auth.models import User

def getFileName(request,filename):
    time_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = "%s%s"%(time_now,filename)
    return os.path.join('images/catagory/',new_filename)

class Catagory(models.Model):
    catagory_name = models.CharField(max_length=100)
    description = models.TextField()
    trending = models.BooleanField(default=False)
    image = models.ImageField(upload_to=getFileName, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Products(models.Model):
    name = models.CharField(max_length=100,)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField(null=True,blank=True)
    actuall_price = models.FloatField(null=True,blank=True)
    new_price = models.FloatField(null=True,blank=True)
    vendor = models.CharField(max_length=100, null=True,blank=True)
    image = models.ImageField(upload_to=getFileName,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    trending = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,default='Empty')
    second_name = models.CharField(max_length=100,default='Empty')
    email = models.EmailField(default='Empty')
    phone = models.IntegerField(default=1234567890)
    # age = models.IntegerField(default=21)
    address = models.CharField(max_length=200)

