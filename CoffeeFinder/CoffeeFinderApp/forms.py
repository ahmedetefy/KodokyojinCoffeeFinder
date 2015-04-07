from django import forms 
from CoffeeFinderApp.models import Page, Coffee_page_image, Coffee_item_review, Order
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
	image = forms.ImageField( label='Select an image', required=True)

	class Meta:
		model = Coffee_page_image
		fields = ['image','page','user']

# ImageForm is a form used for uploading images to a certain coffee shop page. It takes an image
# from the user, the one which he will upload, and the page's id



class ReviewForm(forms.ModelForm):
	class Meta:
		model = Coffee_item_review
		fields = ['field','user','coffee_item']




class DeliveryForm(forms.ModelForm):
	coffeeshop_item_id = forms.IntegerField(help_text="Please enter the ID of your favorite Coffee.")
	quantity = forms.IntegerField(min_value = 1, help_text = "Enter a quantity")
	Name = forms.CharField(max_length = 128, help_text = "Enter Your Name")
	phone = forms.CharField(max_length = 128, help_text = "Enter your phone number")

	class Meta:
		model = Order
		fields = ('quantity', 'Name','phone')

class EditStatus(forms.ModelForm):
	id = forms.IntegerField(help_text="Please enter the ID of the Order.")
	status = forms.CharField(max_length = 128, help_text = "Enter the Status of Order")
	class Meta:
		model = Order
		fields = ('id',)
   
#the delivery form for making an order 
#edit status for manager of the page to be able to add status on his order
#Ahmed Etefy 28 - 3954
