# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0011_team_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='away_rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='home_rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
