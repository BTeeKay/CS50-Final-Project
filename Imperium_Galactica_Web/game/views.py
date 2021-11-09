from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate
from .models import Commodity, Fleet, Building, SteelMills, HCollector, ParticleCollider, ShipFactory
from .game import ResourceGather, UpgradeBuilding, FleetBuild


# Create your views here.
def buildings(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
        
    if request.method == "POST":
        test = UpgradeBuilding(request)
        if test:
            player = str(request.user.username)
            build = Building.objects.get(Name=player)
            steel = build.SteelMill + 1
            hydro = build.HCollector + 1
            pc = build.ParticleCollider + 1
            sf = build.ShipFactory + 1
            return render(request, "game/buildings.html", {
                "builds": Building.objects.get(Name=player),
                "steel": SteelMills.objects.get(Level=steel),
                "hydro": HCollector.objects.get(Level=hydro),
                "particle": ParticleCollider.objects.get(Level=pc),
                "ship": ShipFactory.objects.get(Level=sf),
                "message": "Not enough resource"
                }
                )
            

    player = str(request.user.username)
    build = Building.objects.get(Name=player)
    steel = build.SteelMill + 1
    hydro = build.HCollector + 1
    pc = build.ParticleCollider + 1
    sf = build.ShipFactory + 1
    return render(request, "game/buildings.html", {
        "builds": Building.objects.get(Name=player),
        "steel": SteelMills.objects.get(Level=steel),
        "hydro": HCollector.objects.get(Level=hydro),
        "particle": ParticleCollider.objects.get(Level=pc),
        "ship": ShipFactory.objects.get(Level=sf)
    }
    )


def fleets(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    
    message = ""

    if request.method == "POST":
        test = FleetBuild(request)
        if test:
            message = "Not enough Resource"

    player = str(request.user.username)
    fleet = Fleet.objects.get(Name=player)
    build = Building.objects.get(Name=player)
    ship = build.ShipFactory
    
    return render(request, "game/fleets.html", {
        "fleet": fleet,
        "message": message,
        "ship": ship
    })


def game(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    if request.method == "POST":

        ResourceGather(request)

    player = str(request.user.username)
    try:
        comm = str(Commodity.objects.get(Name=player))
    except: 
        comm = "labia"
    
    c = player.strip()
    p = comm.strip()
    
    if p == c:
        return render(request, "game/game.html", {
        "user": request.user,
        "comms": Commodity.objects.get(Name=player),
        "builds": Building.objects.get(Name=player),
        "ships": Fleet.objects.get(Name=player),
        })
    
    else:
        c = Commodity(Name=player)
        d = Building(Name=player)
        e = Fleet(Name=player)
        c.save()
        d.save()
        e.save()
        return render(request, "game/game.html", {
        "user": request.user,
        "comms": Commodity.objects.get(Name=player),
        "builds": Building.objects.get(Name=player),
        "ships": Fleet.objects.get(Name=player),
    })


