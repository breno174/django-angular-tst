from rest_framework import serializers
from .models import Order


# Create your views here.
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ["id"]
        read_only_fields = ["number"]

    def create(self, validated_data):
        if (
            validated_data["zip_from"].__len__() < 8
            or validated_data["zip_to"].__len__() < 8
        ):
            raise Exception("zip field must have a minimum length of 8 characters")
        return Order.objects.create(**validated_data)


class ListOrder(serializers.ListSerializer):
    ...
