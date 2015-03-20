# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0035_coffee_item_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee_item',
            name='name',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
