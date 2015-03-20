from django.shortcuts import render
from django.conf import settings

# Create your views here.
def index(request):
	context_dict = {}
	return render(request, 'CoffeeFinderApp/index.html', context_dict)

def map(request):
	context_dict = {}
	return render(request, 'CoffeeFinderApp/map.html', context_dict)

def shopSubscribe(request):
	context_dict = {'APIkey': settings.GOOGLE_APIKEY,}
	return render(request, 'CoffeeFinderApp/shopSubscribe.html', context_dict)
