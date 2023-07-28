from .serializers import CreateNewFreight
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.views import Response, status
from order.models import Order
from freight.models import Freight


# Create your views here.
class CreateFreghtOrder(ListCreateAPIView):
    serializer_class = CreateNewFreight
    queryset = Freight.objects.all()

    def create(self, request, *args, **kwargs):
        serilizer = self.get_serializer(data=request.data)
        serilizer.is_valid(raise_exception=True)
        self.perform_create(serilizer)
        return Response(serilizer, status.HTTP_201_CREATED)
        # return super().create(request, *args, **kwargs)

    def perform_create(self, serializer: CreateNewFreight):
        print("\nxx", self.request.data, "\n")
        number = self.request.data
        order: Order = Order.objects.get(number=number.number)
        print("\n", order, "\n")
        freight = serializer.create(order=order)
        freight.save()
        # return super().perform_create(serializer)
