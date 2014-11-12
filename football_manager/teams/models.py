from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Match(models.Model):
    div = models.CharField(max_length=6)
    date = models.DateField()
    home_team = models.ForeignKey(Team, related_name='home_team')
    away_team = models.ForeignKey(Team, related_name='away_team')
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()
    result = models.CharField(max_length=1)

    def __str__(self):
        return "%s vs %s" % (self.home_team, self.away_team)
