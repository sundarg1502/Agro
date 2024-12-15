from django.db import models
import os
import datetime

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
    name = models.CharField(max_length=100)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField(null=True,blank=True)
    actuall_price = models.FloatField(null=True,blank=True)
    new_price = models.FloatField(null=True,blank=True)
    vendor = models.CharField(max_length=100, null=True,blank=True)
    image = models.ImageField(upload_to=getFileName,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    trending = models.BooleanField(default=False)

