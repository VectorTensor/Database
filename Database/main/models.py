from django.db import models

# Create your models here.

class Data(models.Model):
    EntryName= models.CharField(max_length=64)
    Description=models.CharField(max_length=500)
    Image=models.ImageField(upload_to='DataImages',blank=True,null=True)




