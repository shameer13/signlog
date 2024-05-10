from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def loginfun(request):
    if request.method=="POST":
        name=request.POST["txtname"]
        password=request.POST["password"]
        user = authenticate(username=name,password=password)
        if user is not None:
            if user.is_superuser:
                return HttpResponse("welcome to dashboard")
        else:
            data = {"msg": True}
            return render(request,'login.html', data)

    return render(request,'login.html')


def signinfun(request):
    if request.method=="POST":
        name=request.POST["txtname"]
        email=request.POST["txtmail"]
        password=request.POST["password"]
        if User.objects.filter(Q(username=name)|Q(email=email)|Q(password=password)).exists():
            return render(request,'signin.html')
        else:
            u1=User.objects.create_superuser(username=name,email=email,password=password)
            u1.save()
            return redirect('log')

    return render(request,'signin.html')