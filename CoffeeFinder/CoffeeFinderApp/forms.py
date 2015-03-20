from django import forms 
from CoffeeFinderApp.models import Coffee_item


class Coffee_item_form(forms.ModelForm):

	class Meta:
		model = Coffee_item
		fields = ['name', 'price']

# ' Coffee_item form model ' for addition of coffee items through user's suitable interface .
# By using this form a coffee shop owner could add as much coffee items to his page as he/she desire.
# Kareem Tarek 28-1181 .

