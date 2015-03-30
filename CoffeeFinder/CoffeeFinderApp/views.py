from django.conf import settings
from django.shortcuts import render
from CoffeeFinderApp.models import Coffee_item,Page,UserProfile
from django.http import HttpResponseRedirect,HttpResponse
from django.core.context_processors import csrf
from forms import Page_form , UserForm , ReviewForm
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout






def index(request):
	context_dict = {}
	return render(request, 'CoffeeFinderApp/index.html', context_dict)

def map(request):

    categ_list = Page.objects.all()
    context_dict = {'coffeeshops' : categ_list}
    return render(request, 'CoffeeFinderApp/map.html', context_dict)


def shopSubscribe(request):

    context_dict = {'APIkey': settings.GOOGLE_APIKEY,}
    return render(request, 'CoffeeFinderApp/shopSubscribe.html', context_dict)



def page_list(request):

    page_list = Page.objects.all()
    context_dict = {'pages': page_list}

    # Render the response and send it back!
    return render(request, 'CoffeeFinderApp/page_list.html', context_dict)


def coffee_item_page(request, coffee_item_name_id):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        coffee_item = Coffee_item.objects.get(id=coffee_item_name_id)
        context_dict['coffee_item_name'] = coffee_item.name
        context_dict['coffee_item'] = coffee_item

    except Coffee_item.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass
    
    current_user = request.user
    context_dict['user_id'] = current_user.id

    # Go render the response and return it to the client.
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
def post_item_review(request):
    if request.POST:
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/CoffeeFinderApp')
        else:
            form = ReviewForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('CoffeeFinderApp/index.html',args)

def page(request, page_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a page name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        page = Page.objects.get(slug=page_name_slug)
        context_dict['page_name'] = page.name

        # Retrieve all of the associated Coffee items.
        # Note that filter returns >= 1 model instance.
        coffee_items = Coffee_item.objects.filter(page=page)

        # Adds our results list to the template context under name pages.
        context_dict['coffee_items'] = coffee_items
        # We also add the page object from the database to the context dictionary.
        # We'll use this in the template to verify that the page exists.
        context_dict['page'] = page
    except Page.DoesNotExist:
        # We get here if we didn't find the specified page.
        # Don't do anything - the template displays the "no page" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'CoffeeFinderApp/page.html', context_dict)
    #Kareem Tarek 28-1181
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
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


    
 





    
 



