from django.urls import path
from .views import CreateOrderView, ListOrderView, DeleteOrderView, UpdateOrderView

urlpatterns = [
    path("create/", CreateOrderView.as_view()),
    path("list/", ListOrderView.as_view()),
    path("delete/<str:number>/", DeleteOrderView.as_view()),
    path("update/<str:number>/", UpdateOrderView.as_view()),
]
