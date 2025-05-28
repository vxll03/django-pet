from rest_framework import viewsets, permissions

from .models import Category, Event, Location, Ticket
from .serializers import CategorySerializer, EventSerializer, LocationSerializer, TicketSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LocationsViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by("city")
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('event')
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-start_time')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]