from django.shortcuts import render

# Create your views here.
def index(request):
	context_dict = {}
	return render(request, 'CoffeeFinderApp/index.html', context_dict)

def map(request):
	context_dict = {}
	return render(request, 'CoffeeFinderApp/map.html', context_dict)
