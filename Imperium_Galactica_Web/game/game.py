from time import sleep
from .models import PlayerScore, Commodity, Fleet, Building, ParticleCollider, ShipFactory, SteelMills, HCollector
from .resource import ResourceCalc


def CalcScore(request):

    # Takes players ship count, calculates point values and updates PlayerScore database
    player = str(request.user.username)
    fleet = Fleet.objects.get(Name=player)

    try:
        score = PlayerScore.objects.get(Name=player)
    except:
        score = PlayerScore(Name=player)
        score.save()
    
    fighter = (fleet.Fighter * 2) * 2
    heavyfighter = (fleet.HeavyFighter * 6) * 3
    destroyer = (fleet.Destroyer * 17) * 4
    corvette = (fleet.Corvette * 40) * 5
    cruiser = (fleet.Cruiser * 100) * 6
    battleship = (fleet.Battleship * 275) * 7
    total = fighter + heavyfighter + destroyer + corvette + cruiser + battleship
    
    score.Score = total
    score.save()


def FleetBuild(request):
    
    player = str(request.user.username)
    fleet = Fleet.objects.get(Name=player)

    # Check players current Resources against choice of ship
    if request.POST.get("fighter"):
        comm = Commodity.objects.get(Name=player)
        steel = 1000
        hydro = 1000
        anti = 200
        Psteel = comm.Metal
        Phydro = comm.Hydrogen
        Panti = comm.AntiMatter
        if Psteel > steel and Phydro > hydro and Panti > anti:
            fleet.Fighter += 1
            comm.Metal -= steel
            comm.Hydrogen -= hydro
            comm.AntiMatter -= anti
            comm.save()
            fleet.save()
        else:
            return True
    
    if request.POST.get("heavyfighter"):
        comm = Commodity.objects.get(Name=player)
        steel = 3000
        hydro = 3000
        anti = 500
        Psteel = comm.Metal
        Phydro = comm.Hydrogen
        Panti = comm.AntiMatter
        if Psteel > steel and Phydro > hydro and Panti > anti:
            fleet.HeavyFighter += 1
            comm.Metal -= steel
            comm.Hydrogen -= hydro
            comm.AntiMatter -= anti
            comm.save()
            fleet.save()
        
        else:
            return True
    
    if request.POST.get("destroyer"):
        comm = Commodity.objects.get(Name=player)
        steel = 7500
        hydro = 7500
        anti = 2000
        Psteel = comm.Metal
        Phydro = comm.Hydrogen
        Panti = comm.AntiMatter
        if Psteel > steel and Phydro > hydro and Panti > anti:
            fleet.Destroyer += 1
            comm.Metal -= steel
            comm.Hydrogen -= hydro
            comm.AntiMatter -= anti
            comm.save()
            fleet.save()
        else:
            return True
    
    if request.POST.get("corvette"):
        comm = Commodity.objects.get(Name=player)
        steel = 15000
        hydro = 15000
        anti = 10000
        Psteel = comm.Metal
        Phydro = comm.Hydrogen
        Panti = comm.AntiMatter
        if Psteel > steel and Phydro > hydro and Panti > anti:
            fleet.Corvette += 1
            comm.Metal -= steel
            comm.Hydrogen -= hydro
            comm.AntiMatter -= anti
            comm.save()
            fleet.save()
        else:
            return True
        
    if request.POST.get("cruiser"):
        comm = Commodity.objects.get(Name=player)
        steel = 40000
        hydro = 20000
        anti = 40000
        Psteel = comm.Metal
        Phydro = comm.Hydrogen
        Panti = comm.AntiMatter
        if Psteel > steel and Phydro > hydro and Panti > anti:
            fleet.Cruiser += 1
            comm.Metal -= steel
            comm.Hydrogen -= hydro
            comm.AntiMatter -= anti
            comm.save()
            fleet.save()
        else:
            return True
    
    if request.POST.get("battleship"):
        comm = Commodity.objects.get(Name=player)
        steel = 150000
        hydro = 75000
        anti = 50000
        Psteel = comm.Metal
        Phydro = comm.Hydrogen
        Panti = comm.AntiMatter
        if Psteel > steel and Phydro > hydro and Panti > anti:
            fleet.Battleship += 1
            comm.Metal -= steel
            comm.Hydrogen -= hydro
            comm.AntiMatter -= anti
            comm.save()
            fleet.save()
        else:
            return True

def ResourceGather(request):
    
    player = str(request.user.username)
    ResourceCalc(player)


def UpgradeBuilding(request):
    player = str(request.user.username)
    build = Building.objects.get(Name=player)
    comm = Commodity.objects.get(Name=player)

    if request.POST.get("steel"):
        steel = build.SteelMill + 1
        up = SteelMills.objects.get(Level=steel)
        a = up.Steel
        b = up.Hydrogen
        c = up.AntiMatter
        x = comm.Metal
        y = comm.Hydrogen
        z = comm.AntiMatter


        if x > a and y > b and z > c:
            comm.Metal -= up.Steel
            comm.Hydrogen -= up.Hydrogen
            comm.AntiMatter -= up.AntiMatter
            comm.save()
            build.SteelMill += 1
            build.save()
        
        else:
            return True
    
    if request.POST.get("hydrogen"):
        
        hydrogen = build.HCollector + 1
        up = HCollector.objects.get(Level=hydrogen)
        a = up.Steel
        b = up.Hydrogen
        c = up.AntiMatter
        x = comm.Metal
        y = comm.Hydrogen
        z = comm.AntiMatter

        if x > a and y > b and z > c:
            comm.Metal -= up.Steel
            comm.Hydrogen -= up.Hydrogen
            comm.AntiMatter -= up.AntiMatter
            comm.save()
            build.HCollector += 1
            build.save()
        
        else:
            return True

    if request.POST.get("particle"):
        
        particle = build.ParticleCollider + 1
        up = ParticleCollider.objects.get(Level=particle)
        a = up.Steel
        b = up.Hydrogen
        c = up.AntiMatter
        x = comm.Metal
        y = comm.Hydrogen
        z = comm.AntiMatter

        if x > a and y > b and z > c:
            comm.Metal -= up.Steel
            comm.Hydrogen -= up.Hydrogen
            comm.AntiMatter -= up.AntiMatter
            comm.save()
            build.ParticleCollider += 1
            build.save()
        
        else:
            return True
    
    if request.POST.get("ship"):
        
        ship = build.ShipFactory + 1
        up = ShipFactory.objects.get(Level=ship)
        a = up.Steel
        b = up.Hydrogen
        c = up.AntiMatter
        x = comm.Metal
        y = comm.Hydrogen
        z = comm.AntiMatter

        if x > a and y > b and z > c:
            comm.Metal -= up.Steel
            comm.Hydrogen -= up.Hydrogen
            comm.AntiMatter -= up.AntiMatter
            comm.save()
            build.ShipFactory += 1
            build.save()
        
        else:
            return True
        
