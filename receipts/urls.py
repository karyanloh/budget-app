from django.urls import path
from .views import receipt_list

urlpatterns = [
    path("receipts/", receipt_list, name="home"),
]
