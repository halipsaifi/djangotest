from django.db import models

# Create your models here.
ACTIONS = (
    ('not_reviewed', 'Not Reviewed'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
)
class Participant(models.Model):
    name = models.CharField(max_length=80)
    year_born = models.PositiveIntegerField(null=True)
    number_of_siblings = models.PositiveIntegerField(null=True)
    genetic_mutations = models.CharField(max_length=200)
    environmental_exposures = models.CharField(max_length=200)
    status = models.CharField(max_length=14, choices=ACTIONS, default='Not Reviewed')

    def __str__(self):
        return self.name
