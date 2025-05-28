from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoriesViewSet, EventsViewSet, LocationsViewSet, TicketsViewSet

router = DefaultRouter()

router.register(r'categories', CategoriesViewSet, basename='category')
router.register(r'locations', LocationsViewSet, basename='location')
router.register(r'tickets', TicketsViewSet, basename='ticket')
router.register(r'events', EventsViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls))
]