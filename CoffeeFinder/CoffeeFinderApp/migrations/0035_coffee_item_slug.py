# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0034_coffee_item_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee_item',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
