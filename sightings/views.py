from django.shortcuts import render, get_object_or_404, redirect
from .models import Sighting
from .forms import SightingForm
from django.views.generic import UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    context = {"sightings": Sighting.objects.all().order_by('id'), "field_names": Sighting._meta.get_fields()}
    return render(request, 'sightings/index.html',context)

def add_sighting(request):
    #sighting_instance = get_object_or_404(

    if request.method == 'POST':
        form =SightingForm(request.POST)
        if form.is_valid():
            x=form['id'].value()
            sighting = form.save(commit=False)
            # sighting.id = have to get unique squirrel id
            sighting.save()
            return redirect(f'/sightings/{x}')
    else:
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

def stats(request):
    
    total_sightings = Sighting.objects.count()
    gray = Sighting.objects.filter(color='Gray').count()
    cinnamon = Sighting.objects.filter(color='Cinnamon').count()
    black = Sighting.objects.filter(color='Black').count()
    kuks_true = Sighting.objects.filter(kuks=True).count()
    above_ground = Sighting.objects.filter(location='Above Ground').count()
    ground_plane = Sighting.objects.filter(location='Ground Plane').count()
    eating_true = Sighting.objects.filter(eating=True).count()
    adult = Sighting.objects.filter(age='Adult').count()
    juvenile = Sighting.objects.filter(age='Juvenile').count()

    #color = {'gray':gray, 'cinnamon':cinnamon, 'black':black}

    context = {
            'total_sightings': total_sightings,
            'gray': gray,
            'cinnamon': cinnamon,
            'black': black,
            'kuks': kuks_true,
            'above_ground': above_ground,
            'ground_plane': ground_plane,
            'eating_true': eating_true,
            'adult': adult,
            'juvenile': juvenile,
            }
    return render(request, 'sightings/stats.html', context )
