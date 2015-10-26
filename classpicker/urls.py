from django.conf.urls import patterns, url

## base64_pattern = r'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'
base64_pattern = r'([A-Za-z0-9_:-])*'
urlpatterns = patterns('classpicker.views',
    url(r'^start$', 'start', name='start'),
    url(r'^(?P<code>{})$'.format(base64_pattern), 'main', name='main'),
    url(r'^(?P<code>{})/result$'.format(base64_pattern), 'result', name='result'),

)