# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from teams.models import Team

def load_data(apps, schema_editor):
    
    Team.objects.all().delete()
    Team(name="Arsenal").save()
    Team(name="Aston Villa").save()
    Team(name="Burnley").save()
    Team(name="Chelsea").save()
    Team(name="Crystal Palace").save()
    Team(name="Everton").save()
    Team(name="Hull").save()
    Team(name="Leicester").save()
    Team(name="Liverpool").save()
    Team(name="Man City").save()
    Team(name="Man United").save()
    Team(name="Newcastle").save()
    Team(name="QPR").save()
    Team(name="Southampton").save()
    Team(name="Stoke").save()
    Team(name="Sunderland").save()
    Team(name="Swansea").save()
    Team(name="Tottenham").save()
    Team(name="West Brom").save()
    Team(name="West Ham").save()
    

class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20141111_1321'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
