from django.shortcuts import render
from CoffeeFinderApp.models import Coffee_item
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import Coffee_item_form
from django.shortcuts import render_to_response




def index(request):
	context_dict = {}
	return render(request, 'CoffeeFinderApp/index.html', context_dict)

def map(request):
	context_dict = {}
	return render(request, 'CoffeeFinderApp/map.html', context_dict)



def coffee_item_list(request):
	category_list = Coffee_item.objects.order_by('-price')[:10]
	context_dict = {'coffee_items': category_list}
	return render(request, 'CoffeeFinderApp/coffee_item_list.html', context_dict)

    # category_list is assigned a list of ordered 'coffee_item' objects ' Coffee_item.objects.order_by ' . 
    # items are sorted descendingly  with respect to price '('-price')[:10]' i.e most expensive 10 .
    # the test value 10 is just for the current sprint . might be varied later on . 
    # Kareem Tarek 28-1181 




def coffee_item(request, coffee_item_name_slug):

    context_dict = {}

    try:
        # Can we find a coffee_item name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        coffee_item = Coffee_item.objects.get(slug=coffee_item_name_slug)
        context_dict['coffee_item_name'] = coffee_item.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        # Adds our results list to the template context under name pages.
        # We also add the coffee_item object from the database to the context dictionary.
        # We'll use this in the template to verify that the coffee_item exists.
        context_dict['coffee_item'] = coffee_item
    except Coffee_item.DoesNotExist:
        # We get here if we didn't find the specified coffee_item.
        # Don't do anything - the template displays the "no coffee_item" message for us.
        pass

    # Go render the response and return it to the client.
    # Kareem Tarek 28-1181 
    return render(request, 'CoffeeFinderApp/coffee_item.html', context_dict)

def create_coffee_item(request):
    if request.POST:
        form = Coffee_item_form(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/CoffeeFinderApp/coffee_item_list')
    else:
        form = Coffee_item_form()

    args = {}
    args.update(csrf(request))
    args['form']= form
    return render_to_response('CoffeeFinderApp/create_coffee_item.html',args)


# After forms.py is created in its right directory , a ' Coffee_item_form ' is added to the list of forms .
# .. so we could create several instances of Coffee_items manualy . 
# Once form is filled we face two scenarios . whether form is invalid then error messages are displayed , for example" This field is required. "
# Other scenario form is valid . form is then saved and we're redirected to our list of avalaible coffee_items .
# Kareem Tarek 28-1181 

    
 



