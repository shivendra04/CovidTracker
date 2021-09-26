from django.shortcuts import render
from Zones.models import ZoneDetail

# Create your views here.
def get_zone_info(request):
    zone = ZoneDetail.objects.all()
    #if zone.numCases
