# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0053_auto_20150406_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee_item_image',
            name='item',
            field=models.ForeignKey(to='CoffeeFinderApp.Coffee_item'),
            preserve_default=True,
        ),
    ]
