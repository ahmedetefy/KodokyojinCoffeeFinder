from django import forms 
from CoffeeFinderApp.models import Page


class Page_form(forms.ModelForm):

	class Meta:
		model = Page
<<<<<<< HEAD
		fields = ['owner', 'name' , 'latitude', 'longitude', 'area', 'city', 'country', 'street_number']
=======
		fields = ['owner', 'name' , 'longitude', 'latitude','area']
>>>>>>> master

# ' Page form model ' for addition of pages through user's suitable interface .
# By using this form a coffee shop owner could create his page  .
# Kareem Tarek 28-1181 .

