from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('clusterEngine.views',
    url(r'^$', 'main'),
)
