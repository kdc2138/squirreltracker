# Using example from Django tutorial; will replace with proper code
  
from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sighting #as "something" needed?
from django.http import HttpResponse


import csv
import sys

class Command(BaseCommand):
    help = 'Export data to csv'

    def add_arguments(self, parser):
        parser.add_argument('file_path', help='filepath name')

    def handle(self, *args, **options):
        meta = Sighting._meta
        field_names = [f.name for f in meta.fields]
        file_path = options['file_path']
        
        print(file_path)
#        field_names = [field.name for field in meta.fields]

#        response = HttpResponse(content_type='text/csv')
        
#        response['Content-Disposition'] = f"attachment; filename={'file_path'}.csv".format(meta) #need to check if this is the right way to put in file path name
        with open(file_path,'w') as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow(field_names)
            for instance in Sighting.objects.all():
#                writer.writerow([b'\xf0\x9f\x8d\xa9 + \xf0\x9f\x8d\xb5' for field in field_names])
                writer.writerow([getattr(instance, field) for field in field_names])
        
#        return response
