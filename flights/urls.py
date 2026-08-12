from rest_framework.routers import DefaultRouter

from .views import CountryViewSet, AirportViewSet, AirplaneViewSet, AirlineViewSet, CityViewSet, FlightViewSet

router = DefaultRouter()
router.register("countries", CountryViewSet)
router.register("airports", AirportViewSet)
router.register("airlines", AirlineViewSet)
router.register("airplanes", AirplaneViewSet)
router.register("cities", CityViewSet)
router.register("flights", FlightViewSet)


urlpatterns = router.urls