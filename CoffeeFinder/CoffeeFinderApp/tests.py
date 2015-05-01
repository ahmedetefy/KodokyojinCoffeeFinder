from django.test import TestCase
from CoffeeFinderApp.models import Coffee_item ,Page
from forms import Coffee_item_form
from django.core.urlresolvers import reverse
from django import forms 
from CoffeeFinderApp.models import Coffee_page_image
from CoffeeFinderApp.models import Coffee_item_review, Page, Order, PhoneNumbers
from django.core.urlresolvers import reverse

class Coffee_itemTest(TestCase):
	def create_coffee_item(self,name="Frappe"):
	    return Coffee_item.objects.create(
            name = name,
            price=5,
            page = Page.objects.create(
		     owner='kareem',
		     name ='wel3a'
		     ),
            description = "Frappe is delicious"
        )
	def test_coffee_item_creation_and_form_valid(self):
		c = self.create_coffee_item()
		form = Coffee_item_form(data={'name':c.name,'price': c.price,'description': c.description,})
		self.assertTrue(form.is_valid())
		self.assertTrue(isinstance(c,Coffee_item))
		self.assertEqual(c.__unicode__(),c.name)









    # first method in Coffee_itemTest class is used to create instance of coffee item model 
    # second method tests the creation of coffee item instance and
    # validates the form that adds coffee items to a coffeeshop
    # Kareem Tarek 28-1181  


# Create your tests here.



class UploadImageMethodTests(TestCase):

    def test_ensure_coffee_page_images_not_null(self):

        """
                ensure_coffee_page_images_not_null should results True for Images where the image 
                is not null
        """
        
        img = Coffee_page_image(image='map.png',page_id=1, user_id=3)
        img.save()
        self.assertEqual((img.image != 0), True)

class ReviewMethodTests(TestCase):

    def test_ensure_coffee_item_reviews_are_positive(self):

        """
                ensure_reviews_are_positive should results True for reviews where reviews are zero or positive
        """
        rev = Coffee_item_review(field='test', coffee_item_id=1, user_id=0)
        rev.save()
        self.assertEqual((rev.field != 0), True)


    def test_ensure_delivery_option_is_positive(self):
		
		"""
		test_ensure_delevery_option_are_positive should results True when page have delivery option
		"""        
		page = Page(owner='test owner', name='test coffeeshop', delivery=True)
		self.assertEqual(page.delivery, True)

class OrderFormTests(TestCase):

    def test_ensure_order_is_not_null(self):
        """
            test_ensure_order_is_not_null should result True when order is saved in the database
        """
        page = Page(owner='test owner', name='test coffeeshop', delivery=True)
        order = Order(order='Cappucino quantity:1', Name='Rana', phone='01010', deliveryAddress='Roda', Page= page)
        order.save
        self.assertEqual(order.Name, 'Rana')

class AddPhoneNumbersTests(TestCase):

    def test_ensure_phone_number_not_null(self):

        """
                test_ensure_phone_number_not_null should result True for Phone numbers where phone not equal null
        """
        nbr = PhoneNumbers(phone = '0112345678', user_id=4)
        nbr.save()
        self.assertEqual((nbr.phone != 0), True)
