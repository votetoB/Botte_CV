from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'Botte_CV1.views.home', name='home'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^pages/', include('pages.urls', namespace='pages')),
                       url(r'^tournaments/', include('tournament.urls', namespace='tournaments')),
                       url(r'^classpicker/', include('classpicker.urls', namespace='classpicker'))

)
