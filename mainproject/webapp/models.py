from django.db import models

# Create your models here.
class ProductModel(models.Model):
    Productname=models.CharField(max_length=50)
    Productcom=models.CharField(max_length=70)
    Productid=models.IntegerField()
    Productmufc=models.CharField(max_length=70)
    Productcost=models.IntegerField()
