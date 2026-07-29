from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,related_name ="airports")
    def __str__(self):
        return self.name

class Airline(models.Model):
    name = models.CharField(max_length=100)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name ="airlines")
    def __str__(self):
        return self.name

class Airplane(models.Model):
    name = models.CharField(max_length=100)
    seats = models.PositiveIntegerField()

    airline = models.ForeignKey(Airline, on_delete=models.CASCADE,related_name ="airplanes")
    def __str__(self):
        return self.name

class FlightStatus(models.TextChoices):
    SCHEDULED = 'scheduled', 'Scheduled'
    BOARDING = 'boarding', 'Boarding'
    DEPARTED = 'departed', 'Departed'
    DELAYED = 'delayed', 'Delayed'
    CANCELLED = 'cancelled', 'Cancelled'

class Flight(models.Model):
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE,related_name ="flights")
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name ="depatures")
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name ="arrivals")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    status = models.CharField(choices=FlightStatus.choices, max_length=20, default=FlightStatus.SCHEDULED)
    def __str__(self):
        return f"{self.departure_airport} -> {self.arrival_airport}"