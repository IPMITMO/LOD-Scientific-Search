from django.conf.urls import url
from . import views

app_name = 'publications'

urlpatterns = [

    #/publications/
    url(r'^$', views.index, name='index'),

    #/publications/search/smth
    url(r'^search/(?P<search_query>\w+)/$', views.search, name='search'),

    #/publications/id/
    url(r'^(?P<publication_id>[0-9]+)/$', views.detail, name='detail'),
]
#
#Vagranta
#docker
#