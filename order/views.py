from rest_framework.views import APIView, Response, Request, status
from rest_framework.generics import UpdateAPIView, ListAPIView, DestroyAPIView
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


class DeleteOrderView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            order = Order.objects.get(number=self.kwargs.get("order_number"))
        except Exception:
            return Response(
                {"message": "Order not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
