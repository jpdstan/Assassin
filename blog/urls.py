from django.conf.urls import patterns, url
from blog import views

# Must be called urlpatterns for Django to pick up mappings
urlpatterns = patterns('',
	# django.conf.urls.url()
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^add_category/$', views.add_category, name='add_category'),
 	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
 	url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
)