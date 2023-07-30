from django.urls import path
from .views import CreateOrderView, ListOrderView, DeleteOrderView

urlpatterns = [
    path("create/", CreateOrderView.as_view()),
    path("list/", ListOrderView.as_view()),
    path("delete/<str:order_number>/", DeleteOrderView.as_view()),
]
