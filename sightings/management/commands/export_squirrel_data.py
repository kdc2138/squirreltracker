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
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={file_path}.csv'.format(meta) #need to check if this is the right way to put in file path name
        writer = csv.writer(response)

        writer.writerow(field_names)
        for instance in Sighting.objects.all().select_related(): 
            writer.writerow([unicode(getattr(instance, f)).encode('utf-8') for f in field_names])
