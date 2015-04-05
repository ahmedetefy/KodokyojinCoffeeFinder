from django import forms 
from CoffeeFinderApp.models import Page, Order,Coffee_item 
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

class DeliveryForm(forms.ModelForm):
	coffeeshop_item_id = forms.IntegerField(help_text="Please enter the ID of your favorite Coffee.")
	quantity = forms.IntegerField(min_value = 1, help_text = "Enter a quantity")
	Name = forms.CharField(max_length = 128, help_text = "Enter Your Name")
	phone = forms.CharField(max_length = 128, help_text = "Enter your phone number")

	class Meta:
		model = Order
		fields = ('quantity', 'Name','phone')
    
    #class Meta:
    #	model = Order
    #	fields = ('coffeeshop_item', 'quantity','Name','phone')

# ' Page form model ' for addition of pages through user's suitable interface .
# By using this form a coffee shop owner could create his page  .
# Kareem Tarek 28-1181 .

