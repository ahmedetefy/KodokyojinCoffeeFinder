from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    

    def __unicode__(self):
        return self.user.username


class PhoneNumbers(models.Model):

    user = models.OneToOneField(User)
    phone = models.CharField(max_length = 128, null=False)
    
    def __unicode__(self):
       return self.user.username  
#Model phone number has been added each is user is allowed to have one phone number registered
#on system 

class Page(models.Model):
        owner = models.ForeignKey(User)
        name = models.CharField(max_length=128,unique=True)
        delivery = models.BooleanField(default=False)
        longitude = models.DecimalField(max_digits=50, decimal_places=30 ,default=0.0)
        latitude = models.DecimalField(max_digits=50, decimal_places=30 ,default=0.0)
        slug = models.SlugField(unique=True)
        delivery = models.BooleanField(default=False)
        area = models.CharField(max_length=128,default='')
        city = models.CharField(max_length=128,default='')
        country = models.CharField(max_length=128,default='')
        street_number = models.CharField(max_length=12,default=0)
        description = models.CharField(max_length=500,default='')
        verified = models.BooleanField(default=0)



        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Page, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.name

#boolean feila added to Page to make the owner able to add delivery option to his coffeeshop


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

# Kareem Tarek 


# Coffee_item_image model is used to attach one or more image to each Coffee_item model 
# Use of item foreign key makes sure that an image should belong to a single Coffee item 
# page foreign key specifies the page the Coffee item belongs to 
# Kareem Tarek 


class Coffee_page_image(models.Model):
        image = models.ImageField(upload_to='Coffee_page_images', null=False)
        page = models.ForeignKey(Page)
        user = models.ForeignKey(User)

        def __unicode__(self):
                return self.name
# Coffee_page_image model is for images uploaded to coffee shop pages by users.

class Coffee_item_review(models.Model):
    field = models.TextField(max_length=400, null = False)
    coffee_item = models.ForeignKey(Coffee_item)
    user = models.ForeignKey(User)



# Order model takes: order which is the summary of the order, Name which is the name of the user,
# phone and delieveryAddress,
# Order belongs to a CoffeePage
class Order(models.Model):
        order = models.CharField(max_length = 500, default='')
        Name = models.CharField(max_length = 128, default = '')
        phone = models.CharField(max_length = 128, default = '')
        deliveryAddress = models.CharField(max_length = 128, default = '')
        status = models.CharField(max_length = 128, default = 'pending')
        Page = models.ForeignKey(Page)


class Favourite(models.Model):
    user = models.ForeignKey(User)
    coffeeshop_item = models.ForeignKey(Coffee_item)
    page = models.ForeignKey(Page)



class Like_Image(models.Model):
    user = models.ForeignKey(User)
    image = models.ForeignKey(Coffee_page_image, related_name='likes')
    create = models.DateTimeField(auto_now_add=True)
"""
Like_Image takes the image and user as a ForeignKey
and the date the image is liked in
"""


class Like_Review(models.Model):
    user = models.ForeignKey(User)
    review = models.ForeignKey(Coffee_item_review, related_name='likes')
    create = models.DateTimeField(auto_now_add=True)
"""
Like_Review takes the review and user as a ForeignKey
and the date the review is liked in
"""

