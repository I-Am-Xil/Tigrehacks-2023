from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You are at the polls index")

def sign_in(request):
    user_email = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=user_email, password=password)
    
    if user is not None:
        login(request, user)
        return HttpResponse("Signed in")