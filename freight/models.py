from django.db import models
import uuid

# Create your models here.
class Freight(models.Model):
    carrier = models.CharField(max_length=255)
    delivery_time = models.DateField(null=False, blank=False)
    delivery_coust = models.FloatField()
    external_freight_id = models.UUIDField(unique=True, primary_key=False, auto_created=True, default=uuid.uuid4)

    order = models.ForeignKey(
        "order.Order", on_delete=models.CASCADE, related_name="order"
    )
