# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0010_remove_team_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='position',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
