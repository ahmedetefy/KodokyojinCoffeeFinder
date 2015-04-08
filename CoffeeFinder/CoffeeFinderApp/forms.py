from django import forms 
from CoffeeFinderApp.models import Page , Coffee_item  , Coffee_item_image 
from django.contrib.auth.models import User


    
class Page_form(forms.ModelForm):

	class Meta:
		model = Page

		fields = ['owner', 'name' , 'latitude', 'longitude', 'area', 'city', 
        'country', 'street_number','description']

class Page_form_edit(forms.ModelForm):

    description = forms.CharField(max_length=200,help_text="Description",
            widget=forms.Textarea(attrs={'cols': 50, 'rows': 8}))

    class Meta:

        model = Page

        fields = ['description']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')




# ' Page form model ' for addition of pages through user's suitable interface .
# By using this form a coffee shop owner could create his page  .
# Kareem Tarek 28-1181 .

class Coffee_item_form(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Item Title")
    price = forms.IntegerField(initial=0,help_text="Price")
    description = forms.CharField(max_length=200,help_text="Description",
            widget=forms.Textarea(attrs={'cols': 50, 'rows': 2}))

    class Meta:
        model = Coffee_item


        fields = ('name', 'price', 'description' )

        exclude = ['page']
        

class ImageForm_item(forms.ModelForm):
    image = forms.ImageField( label='Select an image', )

    class Meta:

      model = Coffee_item_image
      fields = ['image','page','item']


class ImageForm_item_edit(forms.ModelForm):
    image = forms.ImageField( label='Select an image', )

    class Meta:

      model = Coffee_item_image
      fields = ['image','page','item']



