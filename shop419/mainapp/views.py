from django.shortcuts import render
from .models import Product

# to help load the template file
from django.template import loader

# to help return an Http response to the user for any given request
from django.http import HttpResponse

# Create your views here.

def homeView(request):
    # querying the DB and getting a collection of Product class objects from the records
    products = Product.objects.all() # select * from Product;
    # creating a context dictionary to be used to render the template with info
    context = {
        'product_list' : products, # the key we create here, 
                                # will be available as a variable in template design
                                # in 'home.html'
        'current_page' : 'home'
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

def aboutView(request):

    context = {
        'current_page' : 'about'
    }
    template = loader.get_template('about.html')
    return HttpResponse(template.render(context, request))