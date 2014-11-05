from django.conf.urls import patterns, url

from emailclient import views

urlpatterns = patterns('', 

	url(r'^$', views.index, name='index'),
	url(r'^email', views.email, name='email'),
	url(r'^views/email.html/$', views.email, name='views/email.html'),
	url(r'^views/test.html', views.test, name='test'),
	url(r'^logout/', views.logout, name='logout'),
	url(r'^sendMail', views.sendMail, name='sendMail'),
	url(r'^send/', views.send, name='send.html'), 
	url(r'^test/', views.test, name='test.html')
)