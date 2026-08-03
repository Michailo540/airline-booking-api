from rest_framework.viewsets import ModelViewSet
from drf_spectacular.openapi import AutoSchema
from .models import Country, Airport, Airline, Airplane, City,Flight
from .serializers import (
    CountrySerializer,
    AirportSerializer,
    AirlineSerializer,
    AirplaneSerializer,
    CitySerializer,
    FlightSerializer,
)


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    schema = AutoSchema()


class AirportViewSet(ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    schema = AutoSchema()


class AirlineViewSet(ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    schema = AutoSchema()


class AirplaneViewSet(ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    schema = AutoSchema()

class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer