# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20141112_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='point',
            new_name='points',
        ),
    ]
