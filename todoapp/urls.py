from django.conf.urls import patterns, include, url
from views import index

urlpatterns = patterns(
    'todoapp.views',
    url(r'^$', 'index', name='index'),
)
