from rest_framework.urls import path
from freight.views import CreateAndListFreghtOrder


urlpatterns = [path("/", CreateAndListFreghtOrder.as_view())]
