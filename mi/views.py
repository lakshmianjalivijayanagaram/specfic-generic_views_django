from django.shortcuts import render
 
# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1>This is the view for captain of mi</h1>')
def vicecaptain(request):
    return HttpResponse('<h1><marquee>This is the view for vicecaptain of mi<marquee></h1>')