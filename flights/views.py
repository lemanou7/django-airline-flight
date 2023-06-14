from django.shortcuts import render
from .models import Flight
# Create your views here.

def index(request):
    return render(request, "flights/index.html", context={'flights': Flight.objects.all()})

def single_flight(request, single_flight_id):
    flight = Flight.objects.get(id=single_flight_id)
    return render(request, "flights/single_flight.html", context={
        'single_flight': flight,
        "passengers": flight.passengers.all()
        })