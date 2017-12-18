from django import forms
from .models import Participant

class DataForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = ('name', 'year_born', 'number_of_siblings', 'genetic_mutations', 'environmental_exposures')
        labels = {
            'name': 'Full Name',
            'year_born': 'Year Born',
            'number_of_siblings': 'Nomber of Siblings',
            'genetic_mutations': 'Genetic Mutations',
            'environmental_exposures': 'Environmental Exposures',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'name': 'name'}),
            'year_born': forms.NumberInput(attrs={'class': 'form-control', 'name': 'year_born'}),
            'number_of_siblings': forms.NumberInput(attrs={'class': 'form-control', 'name': 'number_of_siblings'}),
            'genetic_mutations': forms.TextInput(attrs={'class': 'form-control', 'name': 'genetic_mutations'}),
            'environmental_exposures': forms.TextInput(attrs={'class': 'form-control', 'name': 'environmental_exposures'}),
        }
