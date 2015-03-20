# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0020_auto_20150320_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee_item',
            name='slug',
            field=models.SlugField(),
            preserve_default=True,
        ),
    ]
