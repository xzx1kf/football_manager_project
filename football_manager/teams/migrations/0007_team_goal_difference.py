# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20141112_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='goal_difference',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
