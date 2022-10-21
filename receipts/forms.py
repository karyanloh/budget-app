from django.forms import ModelForm
from .models import Receipt, ExpenseCategory


class CreateReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = ["vendor", "total", "tax", "date", "category", "account"]


class CreateCategoryForm(ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ["name"]
