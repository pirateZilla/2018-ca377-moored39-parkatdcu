from django.conf.urls import url

from park_at_dcu import views

app_name = 'park_at_dcu'

urlpatterns = [
    url(r'^$', views.index, name='index'),

]
