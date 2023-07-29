from .serializers import CreateNewFreight
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.views import Response, status
from order.models import Order
from freight.models import Freight
import json


# Create your views here.
class CreateAndListFreghtOrder(ListCreateAPIView):
    serializer_class = CreateNewFreight
    queryset = Freight.objects.all()

    def create(self, request, *args, **kwargs):
        number = request.data.get("order_number")
        delivery_time = request.data.get("delivery_time")
        order: Order = Order.objects.get(number=number)
        response = order.delivery_calculation()

        response_data = []
        for carrier_data in response:
            if "error" in carrier_data.keys():
                continue
            freight_data = {
                "carrier": carrier_data["name"],
                "delivery_time": delivery_time,
                "delivery_coust": carrier_data["price"],
            }
            serializer = self.get_serializer(data=freight_data)
            serializer.is_valid(raise_exception=True)
            serializer.save(order=order)
            response_data.append(serializer.data)

        return Response(response_data, status=status.HTTP_201_CREATED)
