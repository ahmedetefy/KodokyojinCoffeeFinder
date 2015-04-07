from django.test import TestCase
from CoffeeFinderApp.models import Coffee_item_review, Page
from django.core.urlresolvers import reverse
# Create your tests here.



class ReviewMethodTests(TestCase):

    def test_ensure_coffee_item_reviews_are_positive(self):

        """
                ensure_reviews_are_positive should results True for reviews where reviews are zero or positive
        """
        rev = Coffee_item_review(field='test', coffee_item_id=1, user_id=0)
        rev.save()
        self.assertEqual((rev.field != 0), True)

    def test_ensure_delivery_option_is_positive_old(self):
		
		"""
		test_ensure_delevery_option_are_positive should results True when page have delivery option
		"""        
		page = Page(owner='test owner', name='test coffeeshop', delivery=True)
		self.assertEqual(page.delivery, True)
