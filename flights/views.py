from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger
# Create your views here.

def index(request):
    return render(request, "flights/index.html", context={'flights': Flight.objects.all()})

def single_flight(request, single_flight_id):
    flight = Flight.objects.get(id=single_flight_id)
    return render(request, "flights/single_flight.html", context={
        'single_flight': flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
        })

def book(request, single_flight_id):
    if request.method == 'POST':
        flight = Flight.objects.get(pk=single_flight_id)
        passenger = Passenger.objects.get(pk= int(request.POST['passenger']))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('single_flight', args=(flight.id,)))
    
