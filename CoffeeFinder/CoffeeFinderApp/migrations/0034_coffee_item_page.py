# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0033_remove_coffee_item_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee_item',
            name='page',
            field=models.ForeignKey(default='', to='CoffeeFinderApp.Page'),
            preserve_default=False,
        ),
    ]
