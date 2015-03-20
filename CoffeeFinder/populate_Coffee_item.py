import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CoffeeFinder.settings')

import django
django.setup()

from CoffeeFinderApp.models import Coffee_item,Page


def populate():

    python_pag= add_page(
        name= 'Starbucks'
       )

    python_pa= add_page(
        name= 'Cilantro'
       )

    django_pag= add_page(
        name= 'Costa'
       )
     

    add_coffee_item(
        page=python_pag,
        name='Mocha',
        price=25
        )


    add_coffee_item(
        page=django_pag,
        name='Mocha',
        price=25
        )




def add_coffee_item(page,name,price):
     c = Coffee_item.objects.get_or_create(page=page, name=name)[0]
     c.price=price
     c.page=page
     c.save()
     return c


def add_page(name , longitude=0.0, latitude=0.0):
     p = Page.objects.get_or_create(name=name)[0]
     p.longitude=longitude
     p.latitude=latitude
     
     p.save()
     return p

# Start execution here!
if __name__ == '__main__':
    print "Starting CoffeeItem population script..."
    populate()

