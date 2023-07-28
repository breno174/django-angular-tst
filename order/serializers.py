from rest_framework import serializers
from .models import Order


# Create your views here.
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ["id"]
        read_only_fields = ["number"]

    def create(self, validated_data):
        return Order.objects.create(**validated_data)


class ListOrder(serializers.ListSerializer):
    ...
