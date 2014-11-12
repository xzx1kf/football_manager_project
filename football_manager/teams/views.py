#from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template import loader

from teams.models import Team

# Create your views here.
def index(request):
    teams = Team.objects.order_by('name')
    template = loader.get_template('teams/index.html')
    context = RequestContext(request, {
        'teams': teams,
    })
    return HttpResponse(template.render(context))
