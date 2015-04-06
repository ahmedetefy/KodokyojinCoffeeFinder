from django.test import TestCase
from CoffeeFinderApp.models import Coffee_page_image
from django.core.urlresolvers import reverse
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
