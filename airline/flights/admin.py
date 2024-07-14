from django.contrib import admin
from .models import Flight, Airport, passenger
# Register your models here.
class FlightAdmin(admin.ModelAdmin):
  list_display = ("id", "origin", "destination", "duration")
 #changes how the display is on flights.
 

class PassengerAdmin(admin.ModelAdmin):
  filter_horizontal = ("flights",)
  #makes it easy to manipulates flihts chosen by passengers
  
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(passenger, PassengerAdmin)