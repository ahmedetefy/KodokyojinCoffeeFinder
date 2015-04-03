from django import forms 
from CoffeeFinderApp.models import Page, Coffee_page_image 
from django.contrib.auth.models import User



class Page_form(forms.ModelForm):

	class Meta:
		model = Page

		fields = ['owner', 'name' , 'latitude', 'longitude', 'area', 'city', 'country', 'street_number']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')



# ' Page form model ' for addition of pages through user's suitable interface .
# By using this form a coffee shop owner could create his page  .
# Kareem Tarek 28-1181 .

class ImageForm(forms.ModelForm): 
	image = forms.ImageField( label='Select an image', )
	class Meta:
		model = Coffee_page_image
		fields = ['image','page','user']

# ImageForm is a form used for uploading images to a certain coffee shop page. It takes an image
# from the user, the one which he will upload, and the page's id