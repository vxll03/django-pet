from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Note, Test
from .serializers import TestSerializer, NoteSerializer

# Create your views here.
class TestView(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class NoteView(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
