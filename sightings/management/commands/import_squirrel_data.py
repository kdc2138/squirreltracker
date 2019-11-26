# Using example from Django tutorial; will replace with proper code

from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sighting #as "something" needed?
import os
import csv 
from data_import.settings import BASE_DIR
from datetime import datetime

class Command(BaseCommand):
    help = 'Import csv data into database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', help ='file path of csv data')


    def import_data_from_csv(self, filename):
        file_path = options['filename']
        with open(file_path, 'rb') as csv_file:
            data = csv.reader(csv_file, delimiter=',')
            for data_object in data:
               id =  data_object[2]
               age = data_object[7]
               color = data_object[8]
               latitude = data_object[1]
               longitutde = data_object[0]
               date = data_object[5]
               location = data_object[12]
               specific_location = data_object[14]
               running = data_object[15]
               chasing = data_object[16]
               climbing = data_object[17]
               eating = data_object[18]
               foraging = data_object[19]
               other_activites = data_object[20]
               kuks = data_object[21]
               quaas = data_object[22]
               moans = data_object[23]
               tail_flags = data_object[24]
               tail_twitches = data_object[25]
               approaches = data_object[26]
               indifferent = data_object[27]
               runs_from = data_object[28]

               try:
                   sighting, created = Sighting.objects.get_or_create(
                        id=id,
                        age=age,
                        color=color,
                        latitude=latitude,
                        longitude=longitude,
                        date=date,
                        location=location,
                        specific_location=specific_location,
                        running=running,
                        chasing=chasing,
                        climbing=climbing,
                        eating=eating,
                        foraging=foraging,
                        other_activities=other_activities,
                        kuks=kuks,
                        quaas=quaas,
                        moans=moans,
                        tail_flags=tail_flags,
                        tail_twitches=tail_twitches,
                        approaches=approaches,
                        indifferent=indifferent,
                        runs_from=runs_from
                    )
                   if created:
                        sighting.save()
                        display_format = "\nSighting, {}, has been saved."
                            print(display_format.format(movie))
                except Exception as ex:
                    print(str(ex))

    def handle(self, *args, **options):
        self.import_data_from_csv('file_path')









