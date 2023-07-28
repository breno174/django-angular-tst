from rest_framework.urls import path
from freight.views import CreateFreghtOrder


urlpatterns = [path("create/", CreateFreghtOrder.as_view())]
