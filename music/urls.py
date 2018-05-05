from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),

    # /music/71/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail')
]