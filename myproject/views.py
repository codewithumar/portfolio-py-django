from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from myproject.models import Services

# Create your views here.

def index(request):
    con=Services.objects.all()
    return render(request,'index.html',{'context':con})

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        email=request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email Already Used')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'Username Already Used')
            return redirect('register')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('index')
    else:
        return render(request,'register.html')


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


