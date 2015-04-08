from django.test import TestCase
from CoffeeFinderApp.models import Coffee_item ,Page
from forms import Coffee_item_form
from django.core.urlresolvers import reverse
from django import forms 

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
