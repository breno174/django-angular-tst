from rest_framework.views import APIView, Response, Request, status
from rest_framework.generics import UpdateAPIView, ListAPIView
from .serializers import OrderSerializer
from .models import Order
from .serializers import OrderSerializer


# Create your views here.
class CreateOrderView(APIView):
    def post(self, request: Request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"order": serializer.data}, status.HTTP_201_CREATED)


class ListOrderView(ListAPIView):
    def get(self, request: Request):
        orders = Order.objects.all()
        serializer = OrderSerializer(instance=orders, many=True)

        return Response({"stocks": serializer.data}, status.HTTP_200_OK)


class UpdateOrderView(UpdateAPIView):
    ...
