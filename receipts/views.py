from django.shortcuts import render
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def receipt_list(request):
    receipt = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_list": receipt,
    }
    return render(request, "receipts/list.html", context)
