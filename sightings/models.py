from django.db import models

from django.utils.translation import gettext as _

class Sighting(models.Model):

    id = models.CharField(
        help_text=_('Squirrel ID'),
        max_length=255,
        primary_key=True,
    )
    
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
    )

    age = models.CharField(
        help_text=_('Squirel Age'),
        max_length=20,
        choices=AGE_CHOICES,
       # default=ADULT (needs to be blank if not specified so default value not needed?),
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    COLOR_CHOICES = (
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
    )

    color = models.CharField(
        help_text=_('Squirrel Fur Color'),
        max_length=20,
        choices=COLOR_CHOICES,
        # default=? (needs to ba blank if not specified?
    )

    latitude = models.DecimalField(
        help_text=_('Latitude'),
        max_digits=19,
        decimal_places=15, # do we need more decimals places?
    )

    longitude = models.DecimalField(
        help_text=_('Longitude'),
        max_digits=19,
        decimal_places=15, # do we need more decimals places?
    )

    date = models.DateField(
        help_text=_('Sighting Date'),
    )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION_CHOICES = (
        (GROUND_PLANE, 'Ground Plane'),
        (ABOVE_GROUND, 'Above Ground'),
    )

    location = models.CharField(
        help_text=_('Location'),
        max_length=20,
        choices=LOCATION_CHOICES,
        #default=?
    )

    specific_location = models.CharField(
        help_text=_('Specific Location'),
        max_length=255,
    )

    running = models.BooleanField(
        help_text=_('Running'),
        default=False,
    )

    chasing = models.BooleanField(
        help_text=_('Chasing'),
        default=False,
    )

    climbing = models.BooleanField(
        help_text=_('Climbing'),
        default=False,
    )

    eating = models.BooleanField(
        help_text=_('Eating'),
        default=False,
    )

    foraging = models.BooleanField(
        help_text=_('Foraging'),
        default=False,
    )

    other_activities = models.CharField(
        help_text=_('Other Activities'),
        max_length=255,
    )

    kuks = models.BooleanField(
        help_text=_('Kuks'),
        default=False,
    )
   
    quaas = models.BooleanField(
        help_text=_('Quaas'),
        default=False,
    )

    moans = models.BooleanField(
        help_text=_('Moans'),
        default=False,
    )

    tail_flags = models.BooleanField(
        help_text=_('Tail flags'),
        default=False,
    )
   
    tail_twitches = models.BooleanField(
        help_text=_('Tail twitches'),
        default=False,
    )
   
    approaches = models.BooleanField(
        help_text=_('Approaches'),
        default=False,
    )

    indifferent = models.BooleanField(
        help_text=_('Indifferent'),
        default=False,
    )
   
    runs_from = models.BooleanField(
        help_text=_('Runs from'),
        default=False,
    )

    def __str__(self):
        return self.id
# Create your models here.
