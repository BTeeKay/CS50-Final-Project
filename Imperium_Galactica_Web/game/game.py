from time import sleep
from .models import Commodity, Fleet, Building, SteelMills, HCollector


def ResourceGather(request):
    
    player = str(request.user.username)
    resource = Commodity.objects.get(Name=player)

    resource.Metal += 10
    resource.Hydrogen += 5
    resource.AntiMatter += 2
    resource.save()

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
        print(a, b, c, x, y, z)

        if x > a and y > b and z > c:
            print("hello")
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
        
