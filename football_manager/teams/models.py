from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    drawn = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    goals_for = models.IntegerField(default=0)
    goals_against = models.IntegerField(default=0)
    goal_difference = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    position = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Match(models.Model):
    div = models.CharField(max_length=6)
    date = models.DateField()
    home_team = models.ForeignKey(Team, related_name='home_team')
    away_team = models.ForeignKey(Team, related_name='away_team')
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()
    home_rating = models.IntegerField()
    away_rating = models.IntegerField()
    result = models.CharField(max_length=1)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return "%s vs %s" % (self.home_team, self.away_team)
