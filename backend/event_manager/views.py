from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination

from .models import Category, Event, Location, Ticket
from .serializers import CategorySerializer, EventSerializer, LocationSerializer, TicketSerializer

class Pagination(PageNumberPagination):
    # /api/events/?page=1&size=2
    page_size = 10
    max_page_size=100

    page_size_query_param='size'
    page_query_param = 'page'


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    pagination_class = Pagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LocationsViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by("city")
    serializer_class = LocationSerializer
    pagination_class = Pagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('event')
    serializer_class = TicketSerializer
    pagination_class = Pagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-start_time')
    serializer_class = EventSerializer
    pagination_class = Pagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]