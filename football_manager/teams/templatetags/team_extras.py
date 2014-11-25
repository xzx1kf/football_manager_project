from django import template
from django.db.models import Q
from teams.models import Match

register = template.Library()

@register.filter(name='minus')
def minus(value, arg):
    """Subtracts the value of arg from the givin integer"""
    return value - arg
    
@register.filter(name='form')
def form(team_id):
    """Display the result of the most recent 6 matches"""
    matches = Match.objects.filter(Q(home_team=team_id) | Q(away_team=team_id)).order_by('-date')[:6]
    
    form = ""
    for m in matches:
        if m.result == 'H' and m.home_team.id == team_id:
            form += 'W'
        elif m.result == 'A' and m.away_team.id == team_id:
            form += 'W'
        elif m.result == 'D':
            form += 'D'
        else:
            form += 'L'
    
    # Reverse the form so the most recent is on the right.
    return form[::-1]
    
