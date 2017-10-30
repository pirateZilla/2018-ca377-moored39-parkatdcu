from django.conf.urls import url

from . import views

app_name = 'park_at_dcu'

# register the index view
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^webservice/$', views.webservice, name='webservice'),
    url(r'^facility/$', views.facility, name='facility'),
    ]
