from django import forms

from .models import Sighting

class SightingForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'
        #exclude = ['id']

    #def clean_name(self):
        # custom validation for the name field?
