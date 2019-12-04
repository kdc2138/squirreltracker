from django.shortcuts import render, get_object_or_404, redirect
from .models import Sighting
from .forms import SightingForm
from django.views.generic import UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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

class SightingUpdateView(UpdateView):
    model = Sighting
   # fields = '__all__' if we want user to change ID use this line instead of form class
    form_class = SightingForm
    template_name = 'sightings/detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'sighting'

    def form_valid(self,form):
        if 'update' in self.request.POST:
            x = form.save(commit=False)
            x.save()      
            return HttpResponseRedirect(reverse('sightings:index'))
        elif 'delete' in self.request.POST:
            form.instance.delete()
            return HttpResponseRedirect(reverse('sightings:index'))

#def detail(request, id):
    #sighting = get_object_or_404(Sighting, id=pk)
#    sighting = Sighting.objects.get(id=id)
    #if request.method == "POST":
        #form = SightingForm(requesr.POST, instance=sighting)
        #if form.is_valid():
            #sighting = form.save(commit=False)
            #sighting.id = have to get unique squirrel id
            #sighting.save()
            #return redirect('detail', pk=sighting.pk)
    #else:
 #   form = SightingForm(instance=sighting)
 #   context = {"sighting": sighting,}
 #   return render(request, 'sightings/detail.html', {'form': form}, context)

