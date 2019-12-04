from django.urls import path

from . import views

app_name = 'sightings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<id>/',  views.SightingUpdateView.as_view(), name='detail'),
    path('add/', views.add_sighting, name='add_sighting'),
]

#/add/
#/stats/
