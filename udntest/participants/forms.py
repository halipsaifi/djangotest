from django import forms
from .models import Participant

class DataForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = ('name', 'year_born', 'number_of_siblings', 'genetic_mutations', 'environmental_exposures')
