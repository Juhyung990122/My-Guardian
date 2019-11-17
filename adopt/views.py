from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
import random

from .serializer import AdoptSerializer,QuizSerializer
from .models import Adopt,Quiz


class AdoptViewSet(viewsets.ModelViewSet):
    queryset = Adopt.objects.all().order_by('id')
    serializer_class = AdoptSerializer
    

    filter_backends = [SearchFilter]
    search_fields = ('title','body')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all().order_by('?')[:10]
    serializer_class = QuizSerializer

 

    
