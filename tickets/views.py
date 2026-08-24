from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from .models import Ticket
from .serializers import TicketSerializer
from users.permissions import IsOwnerOrAdmin

@extend_schema(tags=['tickets'])
class TicketViewSet(viewsets.ModelViewSet):

    serializer_class = TicketSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.role == 'admin':
            return Ticket.objects.all()
        return Ticket.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
