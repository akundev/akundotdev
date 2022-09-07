from django.urls import path

from .views import OrderCreateView, SuccessView

urlpatterns = [
    path("", OrderCreateView.as_view(), name="order_create"),
    path("success/", SuccessView.as_view(), name="success_created"),
]
