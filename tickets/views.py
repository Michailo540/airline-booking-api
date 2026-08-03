from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from .models import Ticket
from .serializers import TicketSerializer
@extend_schema(tags=['tickets'])
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer