from django.shortcuts import render

# Create your views here.

def adopt(request):
    return render(request, 'adopt/adopt.html' )