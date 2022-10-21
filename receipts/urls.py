from django.urls import path
from .views import receipt_list, create_receipt, category_list, account_list

urlpatterns = [
    path("receipts/", receipt_list, name="home"),
    path("receipts/create/", create_receipt, name="create_receipt"),
    path("receipts/categories/", category_list, name="category_list"),
    path("receipts/accounts/", account_list, name="account_list"),
]
