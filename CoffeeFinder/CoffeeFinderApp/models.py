from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)


    def __unicode__(self):
        return self.user.username
class Page(models.Model):
        owner = models.CharField(max_length=128 , null= False) # Foreign Key to table Owner
        name = models.CharField(max_length=128,unique=True)
        longitude = models.DecimalField(max_digits=50, decimal_places=30 ,default=0.0)
        latitude = models.DecimalField(max_digits=50, decimal_places=30 ,default=0.0)
        slug = models.SlugField(unique=True)
        area = models.CharField(max_length=128,default='')
        city = models.CharField(max_length=128,default='')
        country = models.CharField(max_length=128,default='')
        street_number = models.CharField(max_length=12,default=0)
        description = models.CharField(max_length=500,default='')



       

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
        description = models.CharField(max_length=200)
       

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Coffee_item, self).save(*args, **kwargs)


        def __unicode__(self):
                return self.name

class Coffee_item_image(models.Model):

     image = models.ImageField(upload_to='Coffee_item_images')
     page = models.ForeignKey(Page)
     item = models.ForeignKey(Coffee_item)
 
     def __unicode__(self):
                return self.name


# Since a space is not allowed in a url , presence of slug explicitly eliminates spaces in objects' name for url access  .
# For example , item Mocha Frappe would automatically assigned slug name Mocha-Frappe .
# After assigning a ' space free 'slug name Mocha-Frappe is easily accessed as an individual item through the url 
# http://localhost:8000/CoffeeFinderApp/coffee_item/mocha-frappe/
# Kareem Tarek 28-1181


# Coffee_item_image model is used to attach one or more image to each Coffee_item model 
# Use of item foreign key makes sure that an image should belong to a single Coffee item 
# page foreign key specifies the page the Coffee item belongs to 
# Kareem Tarek 28-1181


