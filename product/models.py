from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    stock = models.IntegerField()
    image = models.URLField()

    def __str__(self):
        return self.name
