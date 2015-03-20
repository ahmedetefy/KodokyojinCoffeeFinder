# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0030_auto_20150320_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee_item',
            name='slug',
            field=models.SlugField(),
            preserve_default=True,
        ),
    ]
