from django.conf.urls import url

from . import views

app_name = 'park_at_dcu'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^webservice/$', views.webservice, name='webservice'),
    url(r'^facility/$', views.facility, name='facility'),
    url(r'^spaces/$', views.spaces, name='spaces'),
    url(r'^occupancy/$', views.occupancy, name='occupancy'),
    url(r'^carpark_for_time/$', views.carpark_for_time, name='carpark_for_time')
    ]

