from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=25,unique=True)
    password=models.CharField(max_length=25,unique=True)

class Products(models.Model):
    product_id=models.CharField(max_length=225,blank=False,primary_key=True,unique=True)
    name=models.CharField(max_length=225,blank=False)
    price=models.IntegerField(max_length=225,blank=False)