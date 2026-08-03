from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                " Price cannot be less than zero."

            )
        return value

    def validate_beggage_weight(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Weight cannot be less than zero."
            )
        return value

    def validate(self, data):
        flight = data.get('flight')
        seat_number = data.get('seat_number')

        if Ticket.objects.filter(seat_number=seat_number).exists():
            raise serializers.ValidationError(
                " Ticket already exists."
            )
        return data