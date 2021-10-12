from django.shortcuts import render

# Create your views here.

def maps_world(request):
    return render(request, 'base.html')