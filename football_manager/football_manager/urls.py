from django.conf.urls import patterns, include, url
from django.contrib import admin
from teams import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'football_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('teams.urls')),
    url(r'^teams/', include('teams.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
