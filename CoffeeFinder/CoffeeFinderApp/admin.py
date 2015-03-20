from django.contrib import admin

from CoffeeFinderApp.models import Coffee_item, Page
from CoffeeFinderApp.models import UserProfile


# Update the registeration to include this customised interface
admin.site.register(Coffee_item)
admin.site.register(Page)
admin.site.register(UserProfile)


# Register Coffee_item and page models so that they can be edited from admin system .
# Kareem Tarek 28-1181 
