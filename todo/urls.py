from django.conf.urls import patterns, url

from todo import views

urlpatterns = patterns('',
	url(r'^home$', views.home, name='home'),
	url(r'^$', views.login, name='login'),
	url(r'^home1/$', views.home1, name='home1'),
	url(r'^notes$', views.notes, name='notes'),
	url(r'^list$', views.list, name='list'),
	url(r'^logout$', views.logout, name='logout')
)
