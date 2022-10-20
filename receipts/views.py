from django.shortcuts import render
from receipts.models import Receipt

# Create your views here.


def receipt_list(request):
    receipt = Receipt.objects.all()
    context = {
        "receipt_list": receipt,
    }
    return render(request, "receipts/list.html", context)
