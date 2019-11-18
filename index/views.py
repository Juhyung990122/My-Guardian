from django.shortcuts import render
from index.models import MyUser

# Create your views here.
def index(request):
    return render(request, 'index/index.html')

