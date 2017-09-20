from django.conf.urls import patterns, url

from park_at_dcu import views

app_name = 'park_at_dcu'

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'))
