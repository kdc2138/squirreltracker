from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
#    path('<int:squirrel_id>/', views.detail, name='detail')
    path('add/', views.add_sighting, name='add_sighting'),
]

#/add/
#/stats/
