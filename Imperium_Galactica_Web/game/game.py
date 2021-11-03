from time import sleep
from .models import Commodity


def ResourceGather(request):
    
    player = str(request.user.username)
    resource = Commodity.objects.get(Name=player)

    resource.Metal += 10
    resource.Hydrogen += 5
    resource.AntiMatter += 2
    resource.save()