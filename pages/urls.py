from django.conf.urls import patterns, url

urlpatterns = patterns('pages.views',

    url(r'^welcome$', 'welcome', name='welcome'),
    url(r'^contacts$', 'contacts', name='contacts'),
    url(r'^hearthstone_school$', 'hearthstone_school', name='hearthstone_school')
)