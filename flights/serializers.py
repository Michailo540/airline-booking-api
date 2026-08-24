from rest_framework import serializers
from .models import (
    Country,
    City,
    Airport,
    Airline,
    Airplane,
    Flight,

)

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"
    def validate_name(self, value):
        if len(value.strip()) <2:
            raise serializers.ValidationError(
                "City must have at least 2 characters."
            )

        if value.isdigit():
            raise serializers.ValidationError(
                'City must only contain letters.'
            )
        return value

class CountrySerializer(serializers.ModelSerializer):
    cities = CitySerializer(many= True, read_only=True)
    class Meta:
        model = Country
        fields = "__all__"
    def validate_name(self, value):
        if len(value.strip()) <2:
            raise serializers.ValidationError(
                "Country must have at least 2 characters."
            )

        if value.isdigit():
            raise serializers.ValidationError(
                'Country must only contain letters.'
            )
        return value



class AirportSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    city = CitySerializer(read_only=True)

    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        source="country",
        write_only=True
    )

    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
        source="city",
        write_only=True
    )

    class Meta:
        model = Airport
        fields = [
            "id",
            "name",
            "country",
            "city",
            "country_id",
            "city_id"
        ]

    def validate_name(self, value):
        if len(value.strip()) <2:
            raise serializers.ValidationError(
                "Airport must have at least 2 characters."
            )
        return value

    def validate(self, data):
        country = data.get("country")
        city = data.get("city")
        if city.country != country:
            raise serializers.ValidationError(
                "This city does not belong to the selected country."

            )
        return data



class AirlineSerializer(serializers.ModelSerializer):
    airport = AirportSerializer(read_only=True)
    airport_id = serializers.PrimaryKeyRelatedField(
        queryset=Airport.objects.all(),
        source="airport",
        write_only=True
    )

    class Meta:
        model = Airline
        fields = ["id", "name", "airport", "airport_id"]

    def validate_name(self, value):
        if len(value.strip()) <3:
            raise serializers.ValidationError(
                "Airline must have at least 2 characters."
            )
        return value
    def validate(self, data):
        name = data.get("name")
        airport = data.get("airport")

        if Airline.objects.filter(name__iexact=name, airport=airport).exists():
            raise serializers.ValidationError(
                "Airline already exists."
            )
        return data



class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = "__all__"


    def validate_name(self, value):
        if len(value.strip()) <2:
            raise serializers.ValidationError(
                "Airplane must have at least 2 characters."
            )
        return value
    def validate_seats(self, value):
        if value  <=0:
            raise serializers.ValidationError(
                "Airplane must have at least 1 characters."
            )
        return value
    def validate(self, data):
        name = data.get("name")
        airline = data.get("airline")
        if Airplane.objects.filter(name=name, airline=airline).exists():
            raise serializers.ValidationError(
                "Airline already exists."
            )
        return data

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"

    def validate(self, data):
        departure_airport = data.get("departure_airport")
        arrival_airport = data.get("arrival_airport")
        departure_time = data.get("departure_time")
        arrival_time = data.get("arrival_time")
        airplane = data.get("airplane")

        if departure_airport== arrival_airport:
            raise serializers.ValidationError(
                " Airplane must have the same airport as departure_airoport."

        )
        if arrival_time <= departure_time:
            raise serializers.ValidationError(
                " Airplane must have arrival_time less than departure_time."
            )

        if Flight.objects.filter(
            airplane=airplane,
            departure_time=departure_time).exists():
            raise serializers.ValidationError(
                "Flight already exists."
            )
        return data