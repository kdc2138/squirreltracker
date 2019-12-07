from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from sightings.models import Sighting

# Create your views here.
def index(request):
    template = loader.get_template('map/index.html')
    context = {"sightings": Sighting.objects.all().order_by('?')[:100]}
    return HttpResponse(template.render(context,request))
