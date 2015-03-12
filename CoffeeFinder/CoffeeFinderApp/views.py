from django.shortcuts import render
from CoffeeFinderApp.models import Coffee_item
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import Coffee_item_form
from django.shortcuts import render_to_response




# Create your views here.
def index(request):
	context_dict = {}
	return render(request, 'CoffeeFinderApp/index.html', context_dict)

def map(request):
	context_dict = {}
	return render(request, 'CoffeeFinderApp/map.html', context_dict)



def coffee_item_list(request):
	category_list = Coffee_item.objects.order_by('-price')[:5]
	context_dict = {'coffee_items': category_list}
	return render(request, 'CoffeeFinderApp/coffee_item_list.html', context_dict)




def coffee_item(request, coffee_item_name_slug):

    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        coffee_item = Coffee_item.objects.get(slug=coffee_item_name_slug)
        context_dict['coffee_item_name'] = coffee_item.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        # Adds our results list to the template context under name pages.
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['coffee_item'] = coffee_item
    except Coffee_item.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
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




