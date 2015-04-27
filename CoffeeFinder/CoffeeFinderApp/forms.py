from django import forms 
from CoffeeFinderApp.models import Page, Coffee_page_image, Coffee_item_review, Order,Coffee_item_image ,Coffee_item_review, Coffee_item, Like_Image, Like_Review
from django.contrib.auth.models import User


class Page_form(forms.ModelForm):

	class Meta:
		model = Page
		fields = ['owner', 'name' , 'delivery', 'latitude', 'longitude', 'area', 'city', 'country', 'street_number']
        # delivery added to the page_form 


class Page_form_edit(forms.ModelForm):

    description = forms.CharField(max_length=200, help_text="Description",
    	widget=forms.Textarea(attrs={'cols': 50, 'rows': 8}))

    class Meta:

        model = Page

        fields = ['description']


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


class Like_ImageForm(forms.ModelForm):

	class Meta:
		model = Like_Image
		fields = ('user', 'image')


class Like_ReviewForm(forms.ModelForm):

	class Meta:
		model = Like_Review
		fields = ('user', 'review')
