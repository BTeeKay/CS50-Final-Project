from .models import Commodity, Fleet, Building, SteelMills, HCollector

def ResourceCalc(player):
    
    steelrate = [5, 10, 20, 40, 60, 80, 100, 120, 140, 160, 200, 250, 300, 350, 400, 420, 500, 1000, 2000, 5000, 10000, 25000]
    hydrorate = [5, 10, 15, 30, 50, 70, 90, 100, 120, 140, 160, 180, 200, 220, 240, 260, 400, 700, 1000, 2000, 5000, 10000, 20000, 25000]
    antirate = [4, 10, 15, 25, 40, 60, 80, 100, 120, 140, 160, 200, 250, 300, 350, 400, 450, 500, 550, 1000, 2000, 5000, 10000, 20000, 25000]

    resource = Commodity.objects.get(Name=player)
    building = Building.objects.get(Name=player)
    
    steel = building.SteelMill
    hydro = building.HCollector
    anti = building.ParticleCollider

    resource.Metal += steelrate[steel]
    resource.Hydrogen += hydrorate[hydro]
    resource.AntiMatter += antirate[anti]
    resource.save()

    # totes = [steelrate[steel], hydrorate[hydro], antirate[anti]]

    # return totes