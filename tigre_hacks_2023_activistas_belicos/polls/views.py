from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if email is None:
            messages.info(request, "Email Cant Be None")
            return redirect("register")
        
        if username is None:
            messages.info(request, "Username Cant Be None")
            return redirect("register")

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Used")
                return redirect("register")
            
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Used")
                return redirect("register")
            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            return redirect("login")
        
        messages.info(request, "Passwords don't match")
        return redirect("register")

    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
    
        if (user or password) is None:
            messages.info(request, "Username or Password are wrong")
            return redirect("login")
            
        auth.login(request, user)
        return redirect("/")
    
    return render(request, "login.html")

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    
    return redirect("/")

#* test view
def auth_status(request):
    if request.user.is_authenticated:
        return HttpResponse(f"You are Authenticated {request.user.id}")
    
    return HttpResponse("You are not Authenticated")

def account(request):
    pass

def about(request):
    pass