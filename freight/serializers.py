from rest_framework import serializers
from order.serializers import OrderSerializer
from freight.models import Freight


class CreateNewFreight(serializers.ModelSerializer):
    order = OrderSerializer

    class Meta:
        depth = 1
        model = Freight
        exclude = ["id"]
