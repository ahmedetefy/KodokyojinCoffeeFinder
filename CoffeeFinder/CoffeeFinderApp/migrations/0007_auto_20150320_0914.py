# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0006_coffee_item_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee_item',
            name='page',
            field=models.ForeignKey(to='CoffeeFinderApp.Page'),
            preserve_default=True,
        ),
    ]
