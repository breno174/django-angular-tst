from rest_framework.views import APIView, Response, Request, status
from rest_framework.generics import UpdateAPIView, ListAPIView, DestroyAPIView
from .serializers import OrderSerializer
from .models import Order
from .serializers import OrderSerializer
from drf_spectacular.utils import extend_schema


# Create your views here.
class CreateOrderView(APIView):
    @extend_schema(responses=OrderSerializer)
    def post(self, request: Request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"order": serializer.data}, status.HTTP_201_CREATED)


class ListOrderView(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class UpdateOrderView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "number"


class DeleteOrderView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "number"
