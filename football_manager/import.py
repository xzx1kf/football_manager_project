from django.db import models
import os, django
import csv
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "football_manager.settings")
django.setup()

from teams.models import Team, Match

with open('E0.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)  # skip the header row
    for row in csvreader:

        # add some custom validation\parsing for some of the fields.
        home_team = Team.objects.get(name=row[2])
        away_team = Team.objects.get(name=row[3])

        date = datetime.strptime(row[1], "%d/%m/%y")

        # create the match object
        match = Match(div=row[0], 
          date=date.strftime("%Y-%m-%d"), 
          home_team=home_team,
          away_team=away_team,
          home_goals=row[4],
          away_goals=row[5],
          result=row[6],
          home_rating=0,
          away_rating=0,
          processed=False)

        try:
            # ignore duplicates
            m = Match.objects.get(div=row[0], 
              date=date.strftime("%Y-%m-%d"), 
              home_team=home_team,
              away_team=away_team,
              home_goals=row[4],
              away_goals=row[5],
              result=row[6])
        except Match.DoesNotExist:
            print "Saving match"
            match.save()
        except Match.MultipleObjectsReturned:
            print "Matches more than one match"
        except:
            print "Match exists already"
