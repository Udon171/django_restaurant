from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world! This is my first Django view.")
    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse("Restaurant")