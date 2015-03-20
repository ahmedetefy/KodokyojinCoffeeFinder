# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0024_auto_20150320_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee_item',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='coffee_item',
            unique_together=set([('name', 'slug', 'page')]),
        ),
    ]
