from django import forms 
from CoffeeFinderApp.models import Page, Coffee_page_image, Coffee_item_review, Order,Coffee_item_image ,Coffee_item_review, Coffee_item
from django.contrib.auth.models import User


class Page_form(forms.ModelForm):

	class Meta:
		model = Page


		fields = ['owner', 'name' , 'delivery', 'latitude', 'longitude', 'area', 'city', 'country', 'street_number']
		
        # delivery added to the page_form 

class Page_form_edit(forms.ModelForm):

    description = forms.CharField(max_length=200,help_text="Description",
            widget=forms.Textarea(attrs={'cols': 50, 'rows': 8}))

    class Meta:

        model = Page

        fields = ['description']

class Page_verification_form(forms.ModelForm):
    
    # verified = forms.BooleanField(widget= forms.HiddenInput())

    class Meta:

        model = Page

        fields = ['verified']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    
    #class Meta:
    #	model = Order
    #	fields = ('coffeeshop_item', 'quantity','Name','phone')


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

class ChangeStatus(forms.ModelForm):
	id = forms.IntegerField(help_text="Please enter the ID of the Order.")
	status = forms.CharField(max_length = 128, help_text = "Enter the Status of Order")
	class Meta:
		model = Order
		fields = ('id','status',)





class EditStatus(forms.ModelForm):
	id = forms.IntegerField(help_text="Please enter the ID of the Order.")
	status = forms.CharField(max_length = 128, help_text = "Enter the Status of Order")
	class Meta:
		model = Order
		fields = ('id',)


class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('order','Name','phone','deliveryAddress','Page')
   


class viewCustomerOrders(forms.ModelForm):
	phone = forms.CharField(max_length = 128, help_text = "Enter the Phone Number you ordered with")
	class Meta:
		model = Order
		fields = ('phone',)

