from django.conf.urls.defaults import patterns, include, url
from django.views.static import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^main/', include('clusterEngine.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
