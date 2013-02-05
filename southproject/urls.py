from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('todoapp.urls')),
)

urlpatterns += staticfiles_urlpatterns()

