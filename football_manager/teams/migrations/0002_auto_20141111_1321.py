# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('div', models.CharField(max_length=6)),
                ('date', models.DateField()),
                ('home_goals', models.IntegerField()),
                ('away_goals', models.IntegerField()),
                ('result', models.CharField(max_length=1)),
                ('away_team', models.ForeignKey(related_name=b'away_team', to='teams.Team')),
                ('home_team', models.ForeignKey(related_name=b'home_team', to='teams.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='team',
            name='short_name',
        ),
    ]
