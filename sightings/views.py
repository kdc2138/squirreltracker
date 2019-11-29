from django.shortcuts import render
from .models import Sighting
# Create your views here.
def index(request):
    context = {"sightings": Sighting.objects.all()}
    return render(request, 'sightings/index.html',context)
