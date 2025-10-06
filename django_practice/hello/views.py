from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def hemant(request):
    return HttpResponse("Hello, Hemant!")

def greet(request, name):
    return HttpResponse(f"Hello, {name}!")