from django.conf.urls import patterns, url

from load import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^prof$', views.prof, name='prof'),
    url(r'^prof/degree$', views.degree, name='degree'),
    url(r'^prof/post$', views.post, name='post'),
    url(r'^group$', views.group, name='group'),
    url(r'^group/caf$', views.caf, name='caf'),
    url(r'^group/subgroup$', views.subgroup, name='subgroup'),
    url(r'^loadunit$', views.loadUnit, name='loadunit'),
    url(r'^loadunit/subject$', views.subject, name='subject'),
    url(r'^loadunit/typeload$', views.typeload, name='typeload'),
    url(r'^loadunit/formpass$', views.formpass, name='formpass'),
    url(r'^spread$', views.spread, name='spread'),
    url(r'^report$', views.report, name='report')

)
