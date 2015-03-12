import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CoffeeFinder.settings')

import django
django.setup()

from CoffeeFinderApp.models import Coffee_item


def populate():
    

    add_coffee_item(
        name='Latte',
        price=18)

    add_coffee_item(
        name='Irish',
        price=20)

    add_coffee_item(
        name='Mocha',
        price=25)


    add_coffee_item(
        name='Mocha',
        price=25)

    add_coffee_item(
        name='Mocha-Frappe',
        price=25)



def add_coffee_item(name,price):
     c = Coffee_item.objects.get_or_create(name=name)[0]
     c.price=price
     c.save()
     return c

# Start execution here!
if __name__ == '__main__':
    print "Starting CoffeeItem population script..."
    populate()

