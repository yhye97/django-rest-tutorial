from django.shortcuts import render
from rest_framework import viewsets
from myapp.serializers import PersonSerializer
from myapp.models import Person

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
