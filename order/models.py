from django.db import models

# Create your models here.
class Order(models.Model):
    number = models.UUIDField(unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    wheigth = models.DecimalField(max_digits=10, decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    zip_from = models.CharField(max_length=8)
    zip_to = models.CharField(max_length=8)

    def delivery_calculation():
        ...
