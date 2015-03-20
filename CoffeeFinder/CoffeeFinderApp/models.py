from django.db import models
from django.template.defaultfilters import slugify

class Page(models.Model):
        name = models.CharField(max_length=128,unique=True)
        longitude = models.DecimalField(max_digits=20, decimal_places=10 ,default=0.0)
        latitude = models.DecimalField(max_digits=20, decimal_places=10 ,default=0.0)
        slug = models.SlugField(unique=True)
       

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Page, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.name




class Coffee_item(models.Model):
        name = models.CharField(max_length=128)
        price = models.IntegerField(default=0)
        slug = models.SlugField(unique=False)
        page = models.ForeignKey(Page)
       

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Coffee_item, self).save(*args, **kwargs)


        def __unicode__(self):
                return self.name

# Since a space is not allowed in a url , presence of slug explicitly eliminates spaces in objects' name for url access  .
# For example , item Mocha Frappe would automatically assigned slug name Mocha-Frappe .
# After assigning a ' space free 'slug name Mocha-Frappe is easily accessed as an individual item through the url 
# http://localhost:8000/CoffeeFinderApp/coffee_item/mocha-frappe/
# Kareem Tarek 28-1181

