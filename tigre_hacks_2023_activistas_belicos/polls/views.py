from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . import models
import requests
# Create your views here.

SUSCRITO = True
NOSUSCRITO = False


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
            
            user_create = User.objects.create_user(username=username, email=email, password=password)
            user_create.save()

            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)

            models.Suscripcion.objects.create(user_id=request.user.id, estado_suscripcion=False)

            return redirect("/")
        
        messages.info(request, "Passwords don't match")
        return redirect("register")

    return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
    
        if user is None:
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
    if request.user.is_authenticated:
        suscription_state = models.Suscripcion.objects.get(user_id=request.user.id).estado_suscripcion

        if suscription_state == SUSCRITO:
            mystring = "Estas suscrito"
        else:
            mystring = ""

        return render(request, "account.html")
    
    return redirect("login")


def about(request):
    return render(request, "about.html")


def subscribe(request):
    if not request.user.is_authenticated:
        return redirect("login")

    user_id = request.user.id

    suscription_state = NOSUSCRITO

    if models.Suscripcion.objects.filter(user_id=user_id).exists():
        suscription_state_get = models.Suscripcion.objects.get(user_id=user_id)
        suscription_state = suscription_state_get.estado_suscripcion

    if suscription_state == SUSCRITO:
        return redirect("account")
        
    if request.method == "POST":
        subscribing = request.POST["subscribe"]

        user_filter = models.Suscripcion.objects.filter(user_id=request.user.id)
        user_filter.update(suscription_state=SUSCRITO)

    return render(request, "subscribe.html")


def unsubscribe(request):
    if not request.user.is_authenticated:
        redirect("login")
    
    if models.Suscripcion.objects.get(user_id=request.user.id).exists():
        pass

    return HttpResponse("unsubscribe")


def geocode_access(request):
    if request.method == "POST":

        api_token = "smncf3nvAJtb6AEH-Oc95Q"
        api_link = "https://geocode.search.hereapi.com/v1/geocode?q="

        initial_address = request.POST["initial_address"]
        final_address = request.POST["final_address"]


        initial_address_2 = ""

        for i in initial_address:
            if i == " ":
                initial_address_2 += "+"
            else:
                initial_address_2 += i
        
        final_address_2 = ""
        
        for i in final_address:
            if i == " ":
                final_address_2 += "+"
            else:
                final_address_2 += i

        print(initial_address_2)
        print(final_address_2)

        initial_address_url = f"{api_link}{initial_address_2}&apiKey={api_token}"
        final_address_url = f"{api_link}{initial_address_2}&apiKey={api_token}"

        print(initial_address_url)
        print(final_address_url)

        initial_address_request = requests.get(f"{api_link}{initial_address_2}&apiKey={api_token}")
        final_address_request = requests.get(f"{api_link}{initial_address_2}&apiKey={api_token}")

        return HttpResponse(f"{initial_address_request.text} : {final_address_request.text}")

    
    return render(request, "geocode_access.html")