from django.conf.urls import patterns, url

from load import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^prof$', views.prof, name='prof'),
    url(r'^degree$', views.degree, name='degree'),
    url(r'^post$', views.post, name='post'),
    url(r'^caf$', views.caf, name='caf'),
    url(r'^subject$', views.subject, name='subject'),
    url(r'^typeload$', views.typeload, name='typeload'),
    url(r'^formpass$', views.formpass, name='formpass'),
    url(r'^group$', views.group, name='group'),
    url(r'^spread$', views.spread, name='spread'),
    url(r'^loadunit$', views.loadUnit, name='loadunit'),
)
