from django import forms 
from CoffeeFinderApp.models import Page, Coffee_item_review  
from CoffeeFinderApp.models import Page
from django.contrib.auth.models import User


class Page_form(forms.ModelForm):

	class Meta:
		model = Page

		fields = ['owner', 'name' , 'delivery', 'latitude', 'longitude', 'area', 'city', 'country', 'street_number']

# delivery added to the page_form 


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')



# ' Page form model ' for addition of pages through user's suitable interface .
# By using this form a coffee shop owner could create his page  .
# Kareem Tarek 28-1181 .



class ReviewForm(forms.ModelForm):
	class Meta:
		model = Coffee_item_review
		fields = ['field','user','coffee_item']




