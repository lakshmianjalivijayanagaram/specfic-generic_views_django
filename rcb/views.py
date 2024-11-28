from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1> Virat Kohli is the captain of rcb</h1>')
def vicecaptain(request):
    return HttpResponse('<h1>This is the view for vicecaptain of rcb</h1>') 
