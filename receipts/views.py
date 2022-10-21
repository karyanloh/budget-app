from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from .forms import CreateReceiptForm, CreateCategoryForm, CreateAccountForm

# Create your views here.


@login_required
def receipt_list(request):
    receipt = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_list": receipt,
    }
    return render(request, "receipts/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = CreateReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            form.save()
            return redirect("home")
    else:
        form = CreateReceiptForm()
    context = {"form": form}
    return render(request, "receipts/create.html", context)


@login_required
def category_list(request):
    category = ExpenseCategory.objects.filter(owner=request.user)
    category_count = ExpenseCategory.objects.count()
    context = {
        "category_list": category,
        "count": category_count,
    }
    return render(request, "receipts/category_list.html", context)


@login_required
def account_list(request):
    account = Account.objects.filter(owner=request.user)
    account_count = Account.objects.count()
    context = {
        "account_list": account,
        "count": account_count,
    }
    return render(request, "receipts/account_list.html", context)


@login_required
def create_category(request):
    if request.method == "POST":
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            form.save()
            return redirect("category_list")
    else:
        form = CreateCategoryForm()
    context = {"form": form}
    return render(request, "receipts/create_category.html", context)


@login_required
def create_account(request):
    if request.method == "POST":
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            account = form.save(False)
            account.owner = request.user
            form.save()
            return redirect("account_list")
    else:
        form = CreateAccountForm
        context = {"form": form}
        return render(request, "receipts/create_account.html", context)
