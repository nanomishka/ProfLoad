from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from load import views

urlpatterns = patterns('',
    url(r'^prof/(?P<page>\d+)/$', views.prof, name='prof'),
    url(r'^prof/degree/$', views.degree, name='degree'),
    url(r'^prof/post/$', views.post, name='post'),
    url(r'^group/(?P<page>\d+)/$', views.group, name='group'),
    url(r'^group/caf/$', views.caf, name='caf'),
    url(r'^group/subgroup/(?P<page>\d+)/$', views.subgroup, name='subgroup'),
    url(r'^loadunit/(?P<page>\d+)/$', views.loadUnit, name='loadunit'),
    url(r'^loadunit/subject/(?P<page>\d+)/$', views.subject, name='subject'),
    url(r'^loadunit/typeload/$', views.typeload, name='typeload'),
    url(r'^loadunit/sortload/$', views.sortload, name='sortload'),
    url(r'^loadunit/formpass/$', views.formpass, name='formpass'),
    url(r'^report/$', views.report, name='report'),
    url(r'^clear/$', views.clear, name='clear'),
    url(r'^(?P<page>\d+)/$', views.index, name='index'),
    url(r'^$',  RedirectView.as_view(url='/1/'))
)
