from django.contrib import admin
from .models import Commodity, Building, Fleet, SteelMills, HCollector, ParticleCollider, ShipFactory

# Register your models here.
admin.site.register(Commodity)
admin.site.register(Building)
admin.site.register(Fleet)
admin.site.register(SteelMills)
admin.site.register(HCollector)
admin.site.register(ParticleCollider)
admin.site.register(ShipFactory)