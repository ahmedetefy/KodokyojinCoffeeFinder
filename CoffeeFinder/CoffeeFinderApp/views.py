from django.conf import settings
from django.shortcuts import get_object_or_404
from CoffeeFinderApp.models import Coffee_item,Page,UserProfile, Coffee_page_image, Order, Coffee_item_review,Coffee_item_image, PhoneNumbers,  Favourite, User, Like_Image, Like_Review
from forms import Page_form , UserForm , ReviewForm, EditStatus, ImageForm, viewCustomerOrders, ChangeStatus, OrderForm, Page_verification_form,  addPhoneNumber
from django.shortcuts import render , render_to_response
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseForbidden
from django.core.context_processors import csrf
from forms import Coffee_item_form , Page_form_edit , ImageForm_item ,ImageForm_item_edit , Coffee_item_form_edit
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from forms import Coffee_item_form , Page_form_edit , ImageForm_item ,ImageForm_item_edit , Coffee_item_form_edit
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages




#action called by orderForm, it validates the form and enters the Order in the Order model, 
#then redirects to the coffeeshop page
def order(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("success")
        else:
            form = OrderForm()
            return HttpResponse("error")


def index(request):
    context_dict = {}
    #Retreieve the currently signed in user.
    current_user = request.user
    #Add the result to the template context under the name current_user.
    context_dict['current_user'] = current_user
    user_id = current_user.id
    #Check if current user is signed in
    if request.user.is_authenticated():
        #Retreive coffeeshop where the current user is the owner
        try:
            coffeeshop = Page.objects.get(owner=user_id)
        except Page.DoesNotExist:
            coffeeshop = None
        # Adds our results list to the template context under name pages.
        context_dict['coffeeshop'] = coffeeshop
    return render(request, 'CoffeeFinderApp/index.html', context_dict)

def requests(request):
    context_dict = {}
    pages = Page.objects.filter(verified=0)
    context_dict = {'pages': pages }
    return render(request, 'CoffeeFinderApp/requests.html', context_dict)

def pageVerification(request, page_name_slug):
    context = RequestContext(request)
    page = Page.objects.get(slug= page_name_slug ) 
    owner = User.objects.get(id= page.owner_id)
    context['page']= page
    context['owner']= owner
    request.session['page_id'] = page.id

    if request.POST:
        form = Page_verification_form(request.POST, instance=page)
        if form.is_valid():
                p = form.save(commit=False)
                p.verified = 1
                if 'accept' in request.POST:
                    form.save()
                    messages.success(request, " Page verified ! ")
                    return HttpResponseRedirect(reverse('CoffeeFinderApp.views.page_list'))

                elif 'reject' in request.POST:
                    page.delete()
                    messages.success(request, " Request has been removed ! ")
                    return HttpResponseRedirect(reverse('CoffeeFinderApp.views.requests'))



    else:
        form = Page_verification_form(instance=page)
 
    return render_to_response('CoffeeFinderApp/pageVerification.html', {
        'form': form, }, context)

    # This view is for an Admin to verify requests to create coffeeshop pages by owners
    # page with page_name_slug is fetched from database along with its owner 
    # Then added to context dictionry , sent to template for displaying detailed info about the page
    # In template , an admin decided wether to accept or reject the request 
    # If accept , verified attribute is changed to 1 and admin is redirected to list of coffee shop page
    # To find newly verified page added to the list .
    # If reject , whole page is deleted from the database along with the request . 
    # Kareem Tarek.

def map(request):

    categ_list = Page.objects.all()
    context_dict = {'coffeeshops' : categ_list}
    return render(request, 'CoffeeFinderApp/map.html', context_dict)


def shopSubscribe(request):

    context_dict = {'APIkey': settings.GOOGLE_APIKEY, 'current_user' :  request.user.id,}
    

    return render(request, 'CoffeeFinderApp/shopSubscribe.html', context_dict)

def page_list(request):

    page_list = Page.objects.all()
    context_dict = {'pages': page_list}

    # Render the response and send it back!
    return render(request, 'CoffeeFinderApp/page_list.html', context_dict)

# action called by view favorites url to view user's favorite coffees. It selects the favorite coffees of the 
# current logged in user. It gets the corresponding item and coffee page for that item, Then stores the results
# items and pages array respectively. It adds the two arrays to the context dictionary and passes them to the 
# view_favorites.html and renders to it.
# author Mostafa Mahmoud
def view_favorites(request):
    

    favorites = Favourite.objects.filter(user_id = request.user.id )
    items = []
    pages = []
    for favorite in favorites:
       item = Coffee_item.objects.get(id=favorite.coffeeshop_item_id)
       items.append(item)


    for item in items:
        page = Page.objects.get(id=item.page_id)
        pages.append(page)

    context_dict = { 'items': items, 'pages': pages }
    return render(request, 'CoffeeFinderApp/view_favorites.html', context_dict)


def coffee_item_page(request, coffee_item_name_id):

    context_dict = {}

    try:
       
        coffee_item = Coffee_item.objects.get(id=coffee_item_name_id)
        context_dict['coffee_item_name'] = coffee_item.name
        context_dict['coffee_item'] = coffee_item
        request.session['item_id'] = coffee_item.id
        context_dict['page_id'] = request.session['page_id']
        page = Page.objects.get(id= request.session['page_id'])
        context_dict['page'] = page
        images = Coffee_item_image.objects.filter(item_id= coffee_item.id ,page_id= page.id )
        context_dict['images'] = images
        form = ImageForm_item()
        context_dict['form'] = form
        reviews = Coffee_item_review.objects.filter(coffee_item_id=coffee_item_name_id)
        reviews = []
        for rev in Coffee_item_review.objects.filter(coffee_item_id=coffee_item_name_id):
            if rev.likes.all().filter(user=request.user):
                reviews.append((rev, True))
            else:
                reviews.append((rev, False))
        context_dict['reviews'] = reviews

    except Coffee_item.DoesNotExist:
  
        pass
    
    current_user = request.user
    context_dict['user'] = current_user
    context_dict['user_id'] = current_user.id
    context_dict['username'] = current_user.username
    #check if customer is signed in
    if request.user.is_authenticated():
        #bit to hide or show button if user is signed in
        context_dict['auth']=1
        #checks if the favorite/unfavorite button is clicked
        if(request.GET.get('favbtn')):
            #If clicked a new object is inserted in the model favorite
            favorite=Favourite(user = current_user,coffeeshop_item = coffee_item,page = page)
            favorite.save()
        #checks if the current item already exists in the users favorites
        if (Favourite.objects.filter(user = current_user,coffeeshop_item = coffee_item,page = page).exists()):
            #if it does exist then the button will say remove from favorites
            context_dict['btntxt'] = "Remove from favorites"
        else:
            #if does not exist the button will say add to favorites allowing the user to favorite the item
            context_dict['btntxt'] = "Add to favorites"
    return render(request, 'CoffeeFinderApp/coffee_item_page.html', context_dict)



def create_page(request):

    if request.POST:
        form = Page_form(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/CoffeeFinderApp')
    else:
         form = Page_form()
         
    args = {}
    args.update(csrf(request))
    args['form']= form

    return render_to_response('CoffeeFinderApp/shopSubscribe.html',args)
# After forms.py is created in its right directory , a ' Coffee_item_form ' is added to the list of forms .
# .. so we could create several instances of Coffee_items manualy . 
# Once form is filled we face two scenarios . whether form is invalid then error messages are displayed , for example" This field is required. "
# Other scenario form is valid . form is then saved and we're redirected to our list of avalaible coffee_items .
# Kareem Tarek 28-1181 



#action called by review post form, it validates the form and enters the review in the item review model
def post_item_review(request):

    if request.POST:
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            coffee_item = form.cleaned_data['coffee_item']
            coffee_item_id = coffee_item.id
            return HttpResponseRedirect(reverse('CoffeeFinderApp.views.coffee_item_page', kwargs={'coffee_item_name_id': coffee_item_id}))
            #return HttpResponseRedirect('/CoffeeFinderApp')
        else:
            form = ReviewForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form

    return HttpResponseRedirect('CoffeeFinderApp/page_list')


def view_review(request, review_id):
    context_dict={}
    review = get_object_or_404(Coffee_item_review, pk=review_id)
    coffee_item_id = review.coffee_item_id
    coffee_item = Coffee_item.objects.get(id=coffee_item_id)
    context_dict['review'] = review
    context_dict['review_field'] = review.field
    context_dict['review_id'] = review.id
    context_dict['coffee_item'] = coffee_item
    return render(request,'CoffeeFinderApp/view_review.html',context_dict)
    # view_review to get a review object if it's in the review table else will return error
    # define the fields in the html page by context_dict and link the view to the view_review html page 

def page(request, page_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}
    try:
        # Can we find a page name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        page = Page.objects.get(slug=page_name_slug)
        context_dict['page_name'] = page.name
        context_dict['page_name_slug'] = page_name_slug
        context_dict['page_description'] = page.description
        request.session['page_id'] = page.id

        # Retrieve all of the associated Coffee items.
        # Note that filter returns >= 1 model instance.
        coffee_items = Coffee_item.objects.filter(page=page)
        # Adds our results list to the template context under name pages.
        context_dict['coffee_items'] = coffee_items

        # We also add the page object from the database to the context dictionary.
        # We'll use this in the template to verify that the page exists.
        context_dict['page'] = page
        #Yasser
        #Retrieve all orders that are associated with the current page.

        order = Order.objects.filter(Page_id=page)

        #Add the results to the template context under the name orders.
        context_dict['orders'] = order
        #Retreieve the currently signed in user.
        current_user = request.user
        #Add the result to the template context under the name current_user.
        context_dict['current_user'] = current_user
        #Yasser
        request.session['page_id'] = page.id
        try: # Try to obtain the user's phone number
            phoneInstance= PhoneNumbers.objects.get(user_id = current_user.id) #gets the phonenumbers instance of logged in user
            phone = phoneInstance.phone #gets the actual phone number
            context_dict['phone']  = phone #passes phone number into dictionary
        except: # If the user doesnt have a phone number
            context_dict['phone'] = "" 
        images = Coffee_page_image.objects.filter(page_id =page.id)
        images = []
        for im in Coffee_page_image.objects.filter(page_id=page.id) :
            if im.likes.all().filter(user=current_user.id):
                images.append((im, True))
            else:
                images.append((im, False))
    except Page.DoesNotExist:
        # We get here if we didn't find the specified page.
        # Don't do anything - the template displays the "no page" message for us.
        pass


     # Render list page with the documents and the form 
    context_dict['images'] = images
    form = ImageForm()
    context_dict['form'] = form
    current_user = request.user
    context_dict['user_id'] = current_user.id
    context_dict['username'] = current_user.username
    # Go render the response and return it to the client.
    return render(request, 'CoffeeFinderApp/page.html', context_dict)
    #Kareem Tarek 28-1181

def uploadImage(request):
    context_dict = {}
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            page = form.cleaned_data['page']
            page_name_slug = page.slug
            noImage = False
            context_dict['noImage'] = noImage
            return HttpResponseRedirect(reverse('CoffeeFinderApp.views.page', kwargs={'page_name_slug': page_name_slug}))
        else:
            page_name_slug = Page.objects.get(id=request.session['page_id']).slug
            form = ImageForm()
            noImage = True
            context_dict['noImage'] = noImage
            return HttpResponseRedirect(reverse('CoffeeFinderApp.views.page', kwargs={'page_name_slug': page_name_slug}))
    else:
        form = ImageForm()
    return render(request, 'CoffeeFinderApp/index.html', context_dict)



def makeOrder(request, page_name_slug):
    #pageID = request.session['my_page']
    context_dict = {}
 
    # Get the context from the request.
    page = Page.objects.get(slug=page_name_slug)
    context_dict['myPage'] = page
    context_dict["Coffee"] = Coffee_item.objects.filter(page_id = page.id)
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            myOrder = form.save(commit=False)
            try:
                try:
                    coffee = Coffee_item.objects.get(id=form['coffeeshop_item_id'].value(),page_id = page.id)
                except:
                    return HttpResponse("An incorrect ID was entered.. Order was not Successful")
                myOrder.coffeeshop_item = coffee
                myOrder.coffeeshop = page
            except Order.DoesNotExist:
                # If we get here, the category does not exist.
                # Go back and render the add category form as a way of saying the category does not exist.
                return render_to_response('CoffeeFinderApp/makeOrder.html', {}, context)
            # Now call the index() view.
            # The user will be shown the homepage.
            myOrder.save()
            return HttpResponse('Your Coffee has been ordered')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = DeliveryForm()
    context_dict['form'] = form
    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    v = 'CoffeeFinderApp/makeOrder.html'
    return render_to_response(v, context_dict, context) #TO DO
#done by Ahmed Etefy 28 - 3954



#this view edits the value of the status of a specific Order determined by the ID sent by the request
#to a new specified status
def change_status(request):
    if request.method == 'POST':
        form = ChangeStatus(request.POST)
        if form.is_valid():
            myOrder = form.save(commit=False)
            temp = Order.objects.get(id=form['id'].value())
            temp.status = form['status'].value()
            temp.save()
            #noImage = False
            #context_dict['noImage'] = noImage
            return HttpResponse("success")
            #return HttpResponseRedirect('/CoffeeFinderApp/map')
    else:
        return HttpResponse("error")
#Mostafa Mahmoud



def editStatus(request, page_name_slug):
    context_dict = {}
    page = Page.objects.get(slug=page_name_slug) #get page object from the slug name in url
    context = RequestContext(request) # Get the context from the request.
    current_user = request.user #get the user instance currently logged onto the website
    context_dict['current_user'] = current_user #pass the current user into context dictionary
    # A HTTP POST?
    if request.method == 'POST':
        form = EditStatus(request.POST) #save the form instance into var form
        # Have we been provided with a valid form?
        if form.is_valid():
            # save the form item to x.
            x = form.save(commit=False)
            try:
                temp = Order.objects.get(id=form['id'].value()) #obtain the order object with id passed in form into temp
            except:
                return HttpResponse('Invalid Order ID') #send to a HTTP page with the following text
            temp.status = form['status'].value() #set the status attribute of the temp object to status field passed in form
            temp.save() #update the object instance into the model
            return HttpResponse('Status has been added') #redirect to a HTTP Page that has the following text
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = EditStatus()
    context_dict['form'] = form #pass the form into the context dictionary
    return render_to_response('CoffeeFinderApp/editStatus.html',context_dict,context)
#Done by Ahmed Etefy #28 - 3954





def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            # From this part till the return http response, we login the user automatically
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            context_dict = {}
            current_user = request.user
            context_dict['user_id'] = current_user.id
            return render(request, 'CoffeeFinderApp/add_view_phonenumber.html', context_dict)
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render(request,
            'CoffeeFinderApp/register.html',
            {'user_form': user_form,'registered': registered} )

def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/CoffeeFinderApp/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'CoffeeFinderApp/login.html', {})

def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/CoffeeFinderApp/')


def add_item(request):
    # Get the context from the request.
    context = RequestContext(request)
    slug = Page.objects.get(id=request.session['page_id']).slug
    context['page_slug']= slug
    context['page_name']= Page.objects.get(id=request.session['page_id']).name

 
    # A HTTP POST?
    if request.method == 'POST':
        form = Coffee_item_form(request.POST)



        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            page = Page.objects.get(id=request.session['page_id'])
            item = form.save(commit=False)

            if Coffee_item.objects.filter(name=item.name,page= page):
               messages.error(request, " Item's already on the list  ")
            else:
                if item.price < 0:  
                   messages.error(request, " Invalid price ")
                else: 
                    item.page = page
                    item.save()
                    messages.success(request, " Item added to your list  ")
                   # return HttpResponseRedirect(reverse('CoffeeFinderApp.views.page', kwargs={'page_name_slug': slug}))


      # Send a success message to the template using messages framework.
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.

        form = Coffee_item_form()


    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('CoffeeFinderApp/add_item.html', {'form': form}, context,)

    # Add_item is a form to add new item to a certain page .
    # Since our path to the link to add new item includes url of a page , we use session page_id
    # page_id is passed to template to be inserted of the newly created item 
    # field checks are performed . price should be > 0 and item should be new to the page
    # Pre implemented django messaging system is used to guide user through the form 
    # Kareem Tarek


def description_edit(request):

    context = RequestContext(request)
    page = Page.objects.get(id=request.session['page_id'])
    context['page'] = page

    if request.POST:
        form = Page_form_edit(request.POST, instance=page)
        if form.is_valid():
            form.save()
            messages.success(request, " Info has been edited successfully")
            # If the save was successful, redirect to another page
            # Description attribute of page is fetched to be edited .
            # Kareem Tarek
 

    else:
        form = Page_form_edit(instance=page)
 
    return render_to_response('CoffeeFinderApp/description_edit.html', {
        'form': form, }, context)

def item_edit(request):

    context = RequestContext(request)
    context['page_slug']= Page.objects.get(id=request.session['page_id']).slug
    context['page_name']= Page.objects.get(id=request.session['page_id']).name


    item = Coffee_item.objects.get(id=request.session['item_id'])
    context['item']= item



    if request.POST:
        form = Coffee_item_form_edit(request.POST, instance=item)
        if form.is_valid():
            if item.price < 0:  
                   messages.error(request, " Invalid price ")
            else: 
                form.save()
                messages.success(request, " Item has been edited successfully ")
               # return HttpResponseRedirect(reverse('CoffeeFinderApp.views.coffee_item_page', kwargs={'coffee_item_name_id': item.id}))
 
    else:
        form = Coffee_item_form_edit(instance=item)
 
    return render_to_response('CoffeeFinderApp/item_edit.html', {
        'form': form, }, context)

def delete_item(request, id):
        context_dict = {}
        context_dict['page_slug']= Page.objects.get(id=request.session['page_id']).slug
        context_dict['page_name']= Page.objects.get(id=request.session['page_id']).name
        context_dict['item']= Coffee_item.objects.get(id=id)
        item = Coffee_item.objects.get(pk=id).delete()
        return render(request, 'CoffeeFinderApp/deleted.html', context_dict)

def uploadImage_item(request):
  context_dict = {}

  if request.method == 'POST':
     form = ImageForm_item(request.POST, request.FILES)

     if form.is_valid():

          form.save()
          item = form.cleaned_data['item']
          coffee_item_name_id = item.id

          return HttpResponseRedirect(reverse('CoffeeFinderApp.views.coffee_item_page', kwargs={'coffee_item_name_id': coffee_item_name_id}))
  
  else:
      form = ImageForm_item()
  return render(request, 'CoffeeFinderApp/index.html', context_dict)

def upload_to_item(request):

    context = {}
    page = Page.objects.get(id=request.session['page_id'])
    item = Coffee_item.objects.get(id= request.session['item_id'] )
    context['page_id'] = page.id
    context['item_id'] = item.id
    form = ImageForm_item()
    context['form'] = form

    return render(request, 'CoffeeFinderApp/upload_to_item.html', context)

    # Since our path to the link to upload_to_item ( Upload image to item ) 
    # includes url of a page , url of item ,  we use sessions page_id and item_id 
    # parameters are passed to template to be added to image attributes 
    # In template we're able to browse computer to fetch desired image .
    # Once upload is triggered we're redirected to uploadImage for the actual upload of the image 
    # Necessary form validations are handled there.
    # Kareem Tarek


def delete_photos(request):
    photo_id = request.POST.get('id', '')
    coffee_id = request.POST.get('item_id', '')
    Coffee_item_image.objects.get(id=photo_id).delete()
    return HttpResponseRedirect("/CoffeeFinderApp/coffee_item_page/" + str(coffee_id))

def delete_review(request):
    review_id = request.POST.get('id', '')
    coffee_id = request.POST.get('coffee', '')
    Coffee_item_review.objects.get(id=review_id).delete()
    return HttpResponseRedirect("/CoffeeFinderApp/coffee_item_page/" + str(coffee_id))

    #This view is for deleting a review.
    #It get a request which contains the review id and the coffee id.
    #It deletes the review from the database and then redirect the user to same coffee page by using the coffee id.

def delete_photo_user(request):
    photo_id = request.POST.get('id', '')
    page_id = request.POST.get('page_id', '')
    Coffee_page_image.objects.get(id=photo_id).delete()
    page = Page.objects.get(id=page_id)
    page_name = page.slug
    return HttpResponseRedirect("/CoffeeFinderApp/page/" + page_name)

    #This view is for deleting a photo.
    #It get a request which contains the photo id and the page id. 
    #It deletes the photo from the database and then redirect the user to same coffeeShop page by using the page name slug that we can get from the page id.




def view_orders(request):
        context_dict = {}
        #page = Page.objects.get(slug=page_name_slug) #get page object from the slug name in url
        context = RequestContext(request) # Get the context from the request.
        # A HTTP POST?
        current_user = request.user #get the user instance currently logged onto the website
        if request.user.is_authenticated():#checks to see if a user is logged in
            phoneInstance= PhoneNumbers.objects.get(user_id = current_user.id) #gets the phonenumbers instance
            #of logged in user
            phone = phoneInstance.phone #gets the actual phone number
            context_dict['phone']  = phone #passes phone number into dictionary
        if request.method == 'POST':
            form = viewCustomerOrders(request.POST) #save the form instance into var form
            # Have we been provided with a valid form?
            if form.is_valid():
                # save the form item to x.
                x = form.save(commit=False)
                try:
                    temp = Order.objects.filter(phone__iexact=form['phone'].value()) #obtain the order object with id passed in form into temp
                except:
                    return HttpResponse('Invalid Phone Number') #send to a HTTP page with the following text
                context_dict['orders'] = temp
                return render_to_response('CoffeeFinderApp/viewOrder.html',context_dict,context) #redirect to a HTTP Page that has the following text
            else:
                # The supplied form contained errors - just print them to the terminal.
                print form.errors
        else:
            # If the request was not a POST, display the form to enter details.
            form = viewCustomerOrders()
        context_dict['form'] = form #pass the form into the context dictionary
        return render_to_response('CoffeeFinderApp/VIEW_ORDER.html',context_dict,context)
# Author: Aly Yakan
# This view redirects to a page that views the user's current phone number if he has it
# It will also allow the user to replace/add a phone number
def add_view_phonenumber(request):
    context_dict = {}
    current_user = request.user
    context_dict['user_id'] = current_user.id
    if request.method == 'GET':
        if request.user.is_authenticated(): #checks to see if a user is logged in
            try: # Try to obtain the user's phone number
                phoneInstance= PhoneNumbers.objects.get(user_id = current_user.id) #gets the phonenumbers instance of logged in user
                phone = phoneInstance.phone #gets the actual phone number
                context_dict['phone']  = phone #passes phone number into dictionary
            except: # If the user doesnt have a phone number
                context_dict['phone'] = "" 
            form = addPhoneNumber()
            context_dict['form'] = form
            return render(request, 'CoffeeFinderApp/add_view_phonenumber.html', context_dict)
        else:
            return HttpResponse('CoffeeFinderApp/index.html')
    else: 
        form = addPhoneNumber(request.POST)
        if form.is_valid():
            falseForm = form.save(commit=False)
            try:
                tempNbr = PhoneNumbers.objects.get(user_id = current_user.id)
                tempNbr.phone = form.cleaned_data['phone']
                tempNbr.save()
            except: # Else create a new entry in the model
                tempNbr = PhoneNumbers(user_id = current_user.id, phone = form.cleaned_data['phone'])
                tempNbr.save()
            context_dict['phone'] = form.cleaned_data['phone'] #passes phone number into dictionary
            messages.success(request, " Your data has been edited successfully ! ")
            return render(request, 'CoffeeFinderApp/index.html', context_dict)
        else:
            print form.errors
            try: # Try to obtain the user's phone number
                phoneInstance= PhoneNumbers.objects.get(user_id = current_user.id) #gets the phonenumbers instance of logged in user
                phone = phoneInstance.phone #gets the actual phone number
                context_dict['phone']  = phone #passes phone number into dictionary
            except: # If the user doesnt have a phone number, pass this message
                context_dict['phone'] = "You haven't added a phone number yet" 
            return render(request, 'CoffeeFinderApp/index.html', context_dict)




def like_review(request):
    if request.POST:
        review_id = request.POST['review']
        coffee_item_review = get_object_or_404(
            Coffee_item_review, id=review_id)
        like_review, created = Like_Review.objects.get_or_create(
            user=request.user, review=coffee_item_review)
    return HttpResponseRedirect(
        reverse(
            'coffee_item_page',
            kwargs={'coffee_item_name_id':
            coffee_item_review.coffee_item.id}))


"""
like_review take a request and check if the request is posting and
then call the review_id from the request and get the review using the id
then check if the user did not like this review before then it add the like
with the image id and the user who request
the like then return to the same page
"""


def like_image(request):
    if request.POST:
        image_id = request.POST['image']
        coffee_page_image = get_object_or_404(
            Coffee_page_image, id=image_id)
        like_image, created = Like_Image.objects.get_or_create(
            user=request.user, image=coffee_page_image)
    return HttpResponseRedirect(
        reverse(
            'page', kwargs={'page_name_slug': coffee_page_image.page.slug}))
"""
like_image take a request and check if the request is posting and
then call the image_id from the request and get the image using the id
then check if the user did not like this image before then it add the like
with the image id and the user who request
the like then return to the same page
"""
