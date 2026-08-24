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
from users.permissions import IsAdminOrReadOnly


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    schema = AutoSchema()
    permission_classes = [IsAdminOrReadOnly]


class AirportViewSet(ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    schema = AutoSchema()
    permission_classes = [IsAdminOrReadOnly]


class AirlineViewSet(ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    schema = AutoSchema()
    permission_classes = [IsAdminOrReadOnly]


class AirplaneViewSet(ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    schema = AutoSchema()
    permission_classes = [IsAdminOrReadOnly]

class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAdminOrReadOnly]

class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAdminOrReadOnly]