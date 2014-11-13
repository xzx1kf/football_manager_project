# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_team_goal_difference'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='position',
            field=models.IntegerField(default=None),
            preserve_default=True,
        ),
    ]
