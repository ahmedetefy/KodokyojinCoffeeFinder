# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0040_coffee_item_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='owner',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
