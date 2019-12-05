from django.urls import path

from . import views

app_name = 'sightings'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_sighting, name='add_sighting'),
    path('stats/', views.stats, name = 'stats'),
    path('<id>/',  views.SightingUpdateView.as_view(), name='detail'),
]

#/add/
#/stats/
