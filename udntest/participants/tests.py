from django.test import TestCase
from django.urls import resolve
from .forms import *   # import all forms
from participants.views import add

# Create your tests here.
class DataFormTest(TestCase):
    # root resolve to data form
    def test_root_url_resolves_to_data_form_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, add)

     # Valid Form Data
    def test_DataForm_valid(self):
        form = DataForm(data={'name': 'John Smith', 'year_born': '1978', 'number_of_siblings': '3', 'genetic_mutations': 'test', 'environmental_exposures': 'test'})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = DataForm(data={'name': "John Smith", 'year_born': "0"})
        self.assertFalse(form.is_valid())
