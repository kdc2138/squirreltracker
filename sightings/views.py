from django.shortcuts import render, get_object_or_404, redirect
from .models import Sighting
from .forms import SightingForm

# Create your views here.
def index(request):
    context = {"sightings": Sighting.objects.all(), "field_names": Sighting._meta.get_fields()}
    return render(request, 'sightings/index.html',context)

def add_sighting(request):
    #sighting_instance = get_object_or_404(

   # if request.method == 'POST':
        #form =SightingForm(request.POST)
        #if form.is_valid():
            #sighting = form.save(commit=False)
            #sighting.id = have to get unique squirrel id
            #sighting.save()
            #return redirect('detail', pk='unique_squirrl_id')
   # else:
    form = SightingForm()
    return render(request, 'sightings/add_sighting.html', {'form': form})


#def detail(request, pk):
    #sighting = get_object_or_404(Sighting, pk=pk)
    #if request.method == "POST":
        #form = SightingForm(requesr.POST, instance=sighting)
        #if form.is_valid():
            #sighting = form.save(commit=False)
            #sighting.id = have to get unique squirrel id
            #sighting.save()
            #return redirect('detail', pk=sighting.pk)
    #else:
        #form = SightingForm(instance=sighting)
    #return render(request, 'sightings/add_sighting.html', {'form': form})

