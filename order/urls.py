from django.urls import path
from .views import CreateOrderView, ListOrderView

urlpatterns = [
    path("create/", CreateOrderView.as_view()),
    path("list/", ListOrderView.as_view()),
]
