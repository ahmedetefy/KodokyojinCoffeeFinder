# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0027_coffee_item_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='coffee_item',
            unique_together=set([('name', 'slug', 'page')]),
        ),
    ]
