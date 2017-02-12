from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^tag/(?P<tag_name>\w+)$', views.index, name='tag'),
	url(r'^(?P<article_id>\d)$', views.article_detail, name='article_detail')
]
