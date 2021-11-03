from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate
from time import sleep
from .models import Commodity
from .game import ResourceGather
from threading import Thread

# Create your views here.
def game(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    player = str(request.user.username)
    comm = str(Commodity.objects.get(Name=player))

    if request.method == "POST":

        ResourceGather(request)

    c = player.strip()
    p = comm.strip()
    
    if p == c:
        return render(request, "game/game.html", {
        "user": request.user,
        "comm": Commodity.objects.get(Name=player),
        })
        
            
