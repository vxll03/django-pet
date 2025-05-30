from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import NoteView, TestView


router = DefaultRouter()
router.register(r'note_tests', TestView, basename='note_tests')
router.register(r'notes', NoteView, basename='tests')

urlpatterns = [
    path("", include(router.urls))
]
