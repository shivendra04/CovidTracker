from django.contrib import admin
from Zones.models import ZoneDetail
# Register your models here.
class ZoneResult(admin.ModelAdmin):
    list_display = ['name','pinCode','zoneType','numCases']
admin.site.register(ZoneDetail,ZoneResult)
