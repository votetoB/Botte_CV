from django.conf.urls import patterns, url

urlpatterns = patterns('tournament.views',
    url(r'^$', view='home', name='home'),
    url(r'^(?P<pk>\d+)/$', view='index', name='index'),
    url(r'^(?P<pk>\d+)/bracket$', view='bracket', name='bracket'),

)