from django import forms 
from CoffeeFinderApp.models import Coffee_item


class Coffee_item_form(forms.ModelForm):

	class Meta:
		model = Coffee_item


