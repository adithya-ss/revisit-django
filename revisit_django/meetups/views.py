from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.

def index(request):
    return HttpResponse("This will be displayed on the landing page.")