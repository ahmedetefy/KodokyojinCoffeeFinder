from django.conf.urls import patterns, url
from CoffeeFinderApp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^map/', views.map, name='map'),
        url(r'^shopSubscribe/', views.shopSubscribe, name = 'shopSubscribe'),
        url(r'^create_page/', views.create_page, name='create_page'),
        url(r'^page/(?P<page_name_slug>[\w\-]+)/$', views.page, name='page'),
        url(r'^coffee_item_page/(?P<coffee_item_name_id>[\w\-]+)/$', views.coffee_item_page, name='coffee_item_page'),
        url(r'^page_list/', views.page_list, name='page_list'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^add_item/$', views.add_item, name='add_item'),
        url(r'^description_edit/', views.description_edit, name = 'description_edit'),
        url(r'^item_edit/', views.item_edit, name = 'item_edit'),
        url(r'^delete/(?P<id>\d+)/$', views.delete_item ,name = 'delete_item'),
        url(r'^uploadImage/$', views.uploadImage, name='uploadImage'),
        url(r'^upload_to_item/$', views.upload_to_item, name='upload_to_item'),
        url(r'^delete_photos/(?P<id>\d+)/$', views.delete_photos, name='delete_photos'),


        


        )
