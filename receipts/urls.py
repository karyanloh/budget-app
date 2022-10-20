from django.urls import path
from .views import receipt_list, create_receipt

urlpatterns = [
    path("receipts/", receipt_list, name="home"),
    path("receipts/create/", create_receipt, name="create_receipt"),
]
