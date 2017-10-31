from django.conf.urls import url

from park_at_dcu import views

app_name = 'park_at_dcu'


urlpatterns = [
    url(r'^$', views.index, name='index'),

]

# register the index view
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^webservice/$', views.webservice, name='webservice'),
    url(r'^facility/$', views.facility, name='facility'),
    url(r'^campus/$', views.facility, name='campus'),
    url(r'^occupancy/$', views.facility, name='occupancy'),
    url(r'^carpark_for_time/$', views.facility, name='carpark_for_time'),
    ]

