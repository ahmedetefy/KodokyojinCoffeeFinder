from django.conf.urls import patterns, url
from CoffeeFinderApp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^map/', views.map, name='map'),
        url(r'^create_page/', views.create_page, name='create_page'),
        url(r'^page/(?P<page_name_slug>[\w\-]+)/$', views.page, name='page'),
        url(r'^coffee_item_page/(?P<coffee_item_name_id>[\w\-]+)/$', views.coffee_item_page, name='coffee_item_page'),
        url(r'^page_list/', views.page_list, name='page_list'),




        )
