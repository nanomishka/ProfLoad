from django.conf.urls import patterns, url

from load import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^prof$', views.prof, name='prof'),
    url(r'^prof/degree$', views.degree, name='degree'),
    url(r'^prof/post$', views.post, name='post'),
    url(r'^group$', views.group, name='group'),
    url(r'^group/caf$', views.caf, name='caf'),
    url(r'^subject$', views.subject, name='subject'),
    url(r'^subject/typeload$', views.typeload, name='typeload'),
    url(r'^subject/formpass$', views.formpass, name='formpass'),
    url(r'^subject/loadunit$', views.loadUnit, name='loadunit'),
    url(r'^spread$', views.spread, name='spread'),
)
