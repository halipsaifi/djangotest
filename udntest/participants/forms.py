from django import forms
from .models import Participant

#add forms
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

# for ec-Auth
class ECUserForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'type': 'password'}))
