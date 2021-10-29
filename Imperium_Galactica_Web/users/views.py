from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CreateUserForm

# Create your views here.

def index(request):
    # if user isn't logged in, send them to Login page
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse("login"))
    return render(request, "users/home.html")

def register_view(request):
    # Register form from Django
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))

    return render(request, "users/register.html", {
        "form": form
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid Login, try again"
            })
    
    if request.method == "GET":
        return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out"
    })
