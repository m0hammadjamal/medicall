from django.db import models


class Impression(models.Model):
    image = models.FileField(upload_to="impressions")
    title = models.CharField(max_length=255)
    discription = models.TextField()



class Product(models.Model):
    image = models.FileField(upload_to="products")
    coats = models.CharField(max_length=255)
    title = models.TextField()