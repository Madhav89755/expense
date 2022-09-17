from django.shortcuts import render
from .models import transaction
from .forms import transactionForm

# Create your views here.

def home(request):
    context={}
    context['frm']=transactionForm()
    context['transaction_obj']=transaction.objects.all().order_by('-paid_on')
    if request.method=="POST":
        paid_for = request.POST['paid_for']
        amount = request.POST['amount']
        transaction_type = request.POST['transaction_type']
        category = request.POST['category']
        newObj=transaction(paid_for=paid_for, amount=amount, transaction_type=transaction_type, category=category)
        newObj.save()
    return render(request,'home.html',context)