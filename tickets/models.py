from django.db import models
from django.conf import settings
from flights.models import Flight

class Ticket(models.Model):
    class TicketClass(models.TextChoices):
        STANDARD = 'standard', 'Standard'
        BUSINESS = 'business', 'Business'
    class TicketStatus(models.TextChoices):
        BOOKED = 'booked', 'Booked'
        CANCELLED = 'cancelled', 'Cancelled'
        USED = 'used', 'Used'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="tickets")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE,related_name="tickets")
    ticket_class = models.CharField(max_length=20,choices=TicketClass.choices,default=TicketClass.STANDARD)
    seat_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=20,choices=TicketStatus.choices,default=TicketStatus.BOOKED)
    baggage_weight = models.PositiveIntegerField(default=20)
    meal = models.CharField(max_length = 50, default= "Standard Meal")


    def __str__(self):
        return f"{self.flight} - {self.seat_number}"
