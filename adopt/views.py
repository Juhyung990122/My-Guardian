from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .serializer import AdoptSerializer,QuizSerializer
from .models import Adopt,Quiz
from index.models import MyUser


class AdoptViewSet(viewsets.ModelViewSet):
    queryset = Adopt.objects.all().order_by('id')
    serializer_class = AdoptSerializer
    

    filter_backends = [SearchFilter]
    search_fields = ('title','body')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    #내가 쓴 글
    '''
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qu = qs.filter(author = self.request.user)
        else:
            qs = qs.none()    
        return qs
    '''

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all().order_by('?')[:10]
    serializer_class = QuizSerializer

 

    
