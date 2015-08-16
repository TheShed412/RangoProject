from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',url(r'^$', views.index, name = 'Index'),
                          url(r'^about/', views.about, name = 'About'),
                          url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),)
