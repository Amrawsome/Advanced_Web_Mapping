from django.shortcuts import render

import userLocation.models
from . import models
from userLocation.models import parkingSpot
from django.contrib.gis.geos import Point
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
# Create your views here.



def update_parkingSpot(request):
    try:
        print (request.POST.get('point',''))
        user_parkingspot = models.parkingSpot.objects.get(user=request.user)
        if not user_parkingspot:
            raise ValueError("Can't get User details")
        long = request.POST["longitude"]
        lat = request.POST["latitude"]
        point = request.POST["point"].split(",")
        point = [float(part) for part in point]
        long = str(long)
        lat = str(lat)
        print(long)
        point = Point(point, srid=4326)
        print(point)
        user_parkingspot.lon = long
        user_parkingspot.lat= lat
        user_parkingspot.location = point
        user_parkingspot.save()
        return JsonResponse({"message": f"Set parking to {point.wkt}."}, status=200)
    except Exception as e:
        raise e;


def homeView(request):
    return render(request,'home.html')

def retrieve(request):
    mydata= parkingSpot.objects.all().values_list('lat','lon').get(pk=1)
    context ={'location':mydata}
    return render(request,"home.html",context)
