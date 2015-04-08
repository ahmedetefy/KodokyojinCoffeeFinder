# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0052_auto_20150408_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='coffeeshop',
        ),
        migrations.RemoveField(
            model_name='order',
            name='coffeeshop_item',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
