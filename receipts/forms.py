from django.forms import ModelForm
from .models import Receipt


class CreateReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = ["vendor", "total", "tax", "date", "category", "account"]
