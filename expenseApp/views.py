from django.shortcuts import render, redirect
from .models import transaction
from .forms import transactionForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login/")
def home(request):
    context={}
    context['frm']=transactionForm()
    context['transaction_obj']=transaction.objects.filter(user=request.user).order_by('-paid_on')
    if request.method=="POST":
        paid_for = request.POST['paid_for']
        amount = request.POST['amount']
        transaction_type = request.POST['transaction_type']
        category = request.POST['category']
        newObj=transaction(user=request.user,paid_for=paid_for, amount=amount, transaction_type=transaction_type, category=category)
        newObj.save()
    return render(request,'home.html',context)

@login_required(login_url="/login/")
def delete_item(request,pk):
    member = transaction.objects.get(id=pk).delete()
    print("Item Number ",pk,)
    return redirect('/')

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
                context['message']='Username already exists please try another one!!!'
            else:
                if User.objects.filter(email=email).exists():
                    context['message']='Email already exists please try another one!!!'
                else:
                    if password1==password2:
                        uss = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                        uss.email = request.POST.get('username')
                        uss.save()
                        context['message']='User Registered Successfully Login to Proceed'
                    else:
                        context['message']='Passwords Do not match please Try Again'
        return render(request,'login.html',context)


    pass

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