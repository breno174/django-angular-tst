from .serializers import CreateNewFreight
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.views import Response, status
from order.models import Order
from freight.models import Freight


# Create your views here.
class CreateAndListFreghtOrder(ListCreateAPIView):
    serializer_class = CreateNewFreight
    queryset = Freight.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def perform_create(self, serializer: CreateNewFreight):
        number = self.request.data.get("order_number")
        order: Order = Order.objects.get(number=number)
        # se comunicar com a API e obeter a resposta
        # passar o path na url do path com os dados do Order
        # criar um loop para percorrer as resposta possiveis da API
        ##  calculate delivery_coust com o valor do frete
        ##  alterar o nome do carrier com a resposta da API
        serializer.save(order=order)
