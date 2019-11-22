from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):

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

    def __str__(self):
        return self.id
# Create your models here.
