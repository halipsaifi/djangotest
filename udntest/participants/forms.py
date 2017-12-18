from django import forms
from .models import Participant
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'type': 'password'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password1 = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password1', 'type': 'password'}))
    password2 = forms.CharField(label="Confirm Password", max_length=30,
                                                          widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password2', 'type': 'password'}))



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
