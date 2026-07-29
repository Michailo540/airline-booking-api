from django.contrib import admin
from .models import Country, Airport, Airline, Airplane, Flight


admin.site.register(Country)
admin.site.register(Airport)
admin.site.register(Airline)
admin.site.register(Airplane)
admin.site.register(Flight)
