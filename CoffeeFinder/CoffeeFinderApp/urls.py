from django.conf.urls import patterns, url
from CoffeeFinderApp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^map/', views.map, name='map'),
        url(r'^coffee_item_list/', views.coffee_item_list, name='coffee_item_list'),
        url(r'^coffee_item/(?P<coffee_item_name_slug>[\w\-]+)/$', views.coffee_item, name='coffee_item'),
        url(r'^create_coffee_item/', views.create_coffee_item, name='create_coffee_item')


        

        )
