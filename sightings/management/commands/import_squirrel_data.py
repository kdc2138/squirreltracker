# Using example from Django tutorial; will replace with proper code

from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sighting #as "something" needed?
import os
import csv
from django.conf import settings
#from data_import.settings import BASE_DIR
import datetime as dt

class Command(BaseCommand):
    help = 'Import csv data into database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', help ='file path of csv data')


    def import_data_from_csv(self, filename):
        with open(filename, 'r') as csv_file:
            data = csv.reader(csv_file, delimiter=',')
            headers = next(data)
            for data_object in data:
                id =  data_object[2]
                age = data_object[7]
                color = data_object[8]
                latitude = data_object[1]
                longitude = data_object[0]
                date = dt.datetime.strptime(data_object[5].strip(),'%m%d%Y').date()
                location = data_object[12]
                specific_location = data_object[14]
                pre_running = data_object[15]
                running = True if "true" in pre_running.lower() else False
                pre_chasing = data_object[16]
                chasing = True if "true" in pre_chasing.lower() else False
                pre_climbing = data_object[17]
                climbing  = True if "true" in pre_climbing.lower() else False
                pre_eating = data_object[18]
                eating = True if "true" in pre_eating.lower() else False
                pre_foraging = data_object[19]
                foraging = True if "true" in pre_foraging.lower() else False
                other_activities = data_object[20]
                pre_kuks = data_object[21]
                kuks = True if "true" in pre_kuks.lower() else False
                pre_quaas = data_object[22]
                quaas = True if "true" in pre_quaas.lower() else False
                pre_moans = data_object[23]
                moans  = True if "true" in pre_moans.lower() else False
                pre_tail_flags = data_object[24]
                tail_flags = True if "true" in pre_tail_flags.lower() else False
                pre_tail_twitches = data_object[25]
                tail_twitches  = True if "true" in pre_tail_twitches.lower() else False
                pre_approaches = data_object[26]
                approaches  = True if "true" in pre_approaches.lower() else False
                pre_indifferent = data_object[27]
                indifferent = True if "true" in pre_indifferent.lower() else False
                pre_runs_from = data_object[28]
                runs_from = True if "true" in pre_runs_from.lower() else False
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
                        print(display_format.format(sighting))
                except Exception as ex:
                    print(str(ex))

    def handle(self, *args, **options):
        file_path = options['file_path']
        self.import_data_from_csv(file_path)









