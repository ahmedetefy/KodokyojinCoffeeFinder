from django.test import TestCase
<<<<<<< HEAD
from CoffeeFinderApp.models import Coffee_page_image
=======
from CoffeeFinderApp.models import Coffee_item_review
>>>>>>> master
from django.core.urlresolvers import reverse
# Create your tests here.


<<<<<<< HEAD
class UploadImageMethodTests(TestCase):

    def test_ensure_coffee_page_images_not_null(self):

        """
                ensure_coffee_page_images_not_null should results True for Images where the image 
                is not null
        """
        
        img = Coffee_page_image(image='map.png',page_id=1, user_id=3)
        img.save()
        self.assertEqual((img.image != 0), True)
=======

class ReviewMethodTests(TestCase):

    def test_ensure_coffee_item_reviews_are_positive(self):

        """
                ensure_reviews_are_positive should results True for reviews where reviews are zero or positive
        """
        rev = Coffee_item_review(field='test',coffee_item_id=1, user_id=0)
        rev.save()
        self.assertEqual((rev.field != 0), True)




        
>>>>>>> master
