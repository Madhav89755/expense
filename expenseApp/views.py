from django.shortcuts import render, redirect
from .models import transaction
from .forms import transactionForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum
# Create your views here.

@login_required(login_url="/login/")
def home(request):
    context={}
    context['frm']=transactionForm()
    objs=transaction.objects.filter(user=request.user).order_by('-paid_on')
    context['transaction_obj']=objs
    if request.method=="POST":
        data={}
        form =transactionForm(request.POST)
        if form.is_valid():
            paid_for = request.POST['paid_for']
            amount = request.POST['amount']
            transaction_type = request.POST['transaction_type']
            category = request.POST['category']
            id=request.POST.get('pk')
            if id=="":             
                newObj=transaction(user=request.user,paid_for=paid_for, amount=amount,  transaction_type=transaction_type, category=category)
                data['status']=200
                data['message']="Record Saved Successfully"
            else:
                newObj=transaction.objects.get(id=id)
                newObj.paid_for=paid_for
                newObj.amount=amount
                newObj.transaction_type=transaction_type
                newObj.category=category
                data['status']=200
                data['message']="Record Updated Successfully"
            newObj.save()
            objs=transaction.objects.filter(user=request.user).order_by('-paid_on').values()
            data['transaction_obj']=list(objs)
        else:
            data['status']=202
            data['message']="Failed To Save Record"

        return JsonResponse(data)
        
    return render(request,'home.html',context)

@login_required(login_url="/login/")
def delete_item(request):
    data={}
    if request.method=="POST":
        pk=request.POST['pk']
        member = transaction.objects.get(id=pk).delete()
        print("Item Number ",pk,)
        data['status']=200
        data['message']="Record Deleted Successfully"
    else:
        data['status']=202
        data['message']="Invalid Request"
    return JsonResponse(data)

@login_required(login_url="/login/")
def update_item(request):
    data={}
    id=request.GET['pk']
    try:
        objs=transaction.objects.get(pk=id)
        data['obj']={"category":objs.category,"amount":objs.amount,"paid_for":objs.paid_for,"transaction_type":objs.transaction_type}
        data['status']=200
    except:
        data['status']=202
    return JsonResponse(data)



def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        context={}
        if request.method=="POST":
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            username=request.POST['username']
            password1=request.POST['password1']
            password2=request.POST['password2']
            if User.objects.filter(username=username).exists():
                context["status"]=202
                context["message"]="Username already exists please try another one!!!"
            else:
                if User.objects.filter(email=email).exists():
                    context['status']=202
                    context['message']='Email already exists please try another one!!!'
                else:
                    if password1==password2:
                        uss = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                        uss.email = request.POST.get('username')
                        uss.save()
                        context["status"]=200
                        context["message"]="User Registered Successfully Login to Proceed"
                    else:
                        context["status"]=202
                        context["message"]="Passwords Do not match please Try Again"
        return render(request,'login.html',context)


def username_check(request):
    if request.method=="POST":
        username=request.POST['username']
        if User.objects.filter(username=username).exists():
            return JsonResponse({"status":200,"message":"This username already exists exists"})
        return JsonResponse({"status":202})


def login(request):
    context={}
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                context['message']='Invalid Username or Password Please Check'
        return render(request,'login.html',context)

@login_required(login_url="/login/")
def logout_user(request):
    logout(request)
    return render(request,'login.html',{'message':'User Logged Out Successfully'})

@login_required(login_url="/login/")
def summary(request):
    context={}
    exp_obj=transaction.objects.all()
    abc_obj=exp_obj.values("paid_on__date").distinct("paid_on__date")
    context['exp_obj_transaction']=list(str(x['paid_on__date']) for x in abc_obj)
    
    # debit
    debit_objs=exp_obj.filter(transaction_type="debit").values("paid_on__date").annotate(Sum('amount'))
    context['debit_objs']=list({'paid_on': x['paid_on__date'], 'amount': x['amount__sum']} for x in debit_objs)
    
    # total amount debited
    debit_total_objs=debit_objs.values('amount').aggregate(Sum('amount'))
    context['total_amount_debit']=debit_total_objs['amount__sum']

    # credit
    credit_objs=exp_obj.filter(transaction_type="added").values("paid_on__date").annotate(Sum('amount'))
    context['credit_objs']=list({'paid_on': x['paid_on__date'], 'amount': x['amount__sum']} for x in credit_objs)
    
    # total amount added
    added_total_objs=credit_objs.values('amount').aggregate(Sum('amount'))
    context['total_amount_added']=added_total_objs['amount__sum']
    # total savings
    if debit_total_objs['amount__sum']==None:
        context['saving']=added_total_objs['amount__sum']
    else:
        context['saving']=added_total_objs['amount__sum']-int(debit_total_objs['amount__sum'])


    return render(request,'summary.html',context)