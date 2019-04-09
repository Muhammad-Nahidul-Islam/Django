from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length = 3000)


class offer(models.Model):
    code = models.CharField(max_length = 55)
    description = models.CharField(max_length = 500)
    discount = models.FloatField()
    