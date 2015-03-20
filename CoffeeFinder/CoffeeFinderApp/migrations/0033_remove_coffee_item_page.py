# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0032_remove_coffee_item_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee_item',
            name='page',
        ),
    ]
