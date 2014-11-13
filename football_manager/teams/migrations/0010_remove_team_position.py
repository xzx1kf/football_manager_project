# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0009_auto_20141113_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='position',
        ),
    ]
