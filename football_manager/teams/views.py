from django.shortcuts import render

from teams.models import Team
from teams.models import Match

from elo.elo import Result, EloFootballRating

# Create your views here.
def index(request):
    context = {}
    return render(request, 'teams/index.html', context)

def league(request):
    teams = Team.objects.order_by('-points', '-goal_difference', 'name')
    context = {'teams': teams}
    return render(request, 'teams/league.html', context)

def update(request):
    
    if request.method == 'POST':
        
        # get all unprocessed matches in date order
        matches = Match.objects.filter(processed=False).order_by('date')
        
        # for each match update the team object
        for match in matches:
            
            # get the teams
            home_team = Team.objects.get(name=match.home_team)
            away_team = Team.objects.get(name=match.away_team)
            
            # update played
            home_team.played += 1
            away_team.played += 1
            
            home_team_result = Result.WIN
            away_team_result = Result.LOSE
            
            # updated won/lost/drawn and points
            if match.result == 'H':
                home_team.won += 1
                away_team.lost += 1
                home_team.points += 3
            elif match.result == 'D':
                home_team.drawn += 1
                away_team.drawn += 1
                home_team.points += 1
                away_team.points += 1
                home_team_result = Result.DRAW
                away_team_result = Result.DRAW
            else: # match.result == 'A':
                home_team.lost += 1
                away_team.won += 1
                away_team.points += 3
                home_team_result = Result.LOSE
                away_team_result = Result.WIN
                
            # update goals for/against
            home_team.goals_for += match.home_goals
            home_team.goals_against += match.away_goals
            away_team.goals_for += match.away_goals
            away_team.goals_against += match.home_goals
            
            # update goal difference
            home_team.goal_difference = home_team.goals_for - home_team.goals_against
            away_team.goal_difference = away_team.goals_for - away_team.goals_against
            
            # calculate elo rating
            goal_difference = abs(home_team.goals_for - away_team.goals_against)
            # home
            elo_rating = EloFootballRating(20)
            home_team.rating += elo_rating.calculate(home_team.rating, away_team.rating, goal_difference, home_team_result) 
            
            # away
            away_team.rating += elo_rating.calculate(away_team.rating, home_team.rating, goal_difference, away_team_result) 
            
            # update processed to True
            match.processed = True
            
            home_team.save()
            away_team.save()
            match.save()
    else:
        pass
        
    return render(request, 'teams/update.html')
