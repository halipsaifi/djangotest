# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('year_born', models.PositiveIntegerField(null=True)),
                ('number_of_siblings', models.PositiveIntegerField(null=True)),
                ('genetic_mutations', models.CharField(max_length=200)),
                ('environmental_exposures', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Not Reviewed', 'Not Reviewed'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Not Reviewed', max_length=14)),
            ],
        ),
    ]