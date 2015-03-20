from django.contrib import admin

from CoffeeFinderApp.models import Coffee_item, Page

# Update the registeration to include this customised interface
admin.site.register(Coffee_item)
admin.site.register(Page)

# Register Coffee_item and page models so that they can be edited from admin system .
# Kareem Tarek 28-1181 
