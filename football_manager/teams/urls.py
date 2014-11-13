from django.conf.urls import patterns, url

from teams import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^update/$', views.update, name='update'),
    url(r'^league/$', views.league, name='league'),
    url(r'^team/(?P<team_id>\d+)/$', views.team, name='team'),
)
