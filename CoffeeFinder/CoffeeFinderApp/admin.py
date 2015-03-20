from django.contrib import admin

from CoffeeFinderApp.models import Coffee_item, Page

# Update the registeration to include this customised interface
admin.site.register(Coffee_item)
admin.site.register(Page)

# Register your models here.
