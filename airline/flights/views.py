from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from.models import Flight,passenger

# Create your views here.
def index(request):
  return render(request, "flights/index.html", {
    "flights":Flight.objects.all()
    })
  
def flight(request, flight_id):
  flight = Flight.objects.get(id = flight_id)
  return render(request, "flights/flight.html",{
    "flight": flight,
    "Passenger":flight.passenger.all(),
    "non_passengers": passenger.objects.exclude(flights = flight).all()
  })
  
def book (request, flight_id):
  if request.method == "POST":
    flight = Flight.objects.get(pk=flight_id)
    Passenger = passenger.objects.get(pk=int(request.POST["Passenger"]))
    Passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight.id)))
  