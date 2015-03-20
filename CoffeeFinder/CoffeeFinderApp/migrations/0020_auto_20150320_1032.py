# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0019_auto_20150320_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee_item',
            name='name',
            field=models.CharField(unique=True, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coffee_item',
            name='page',
            field=models.ForeignKey(to='CoffeeFinderApp.Page'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coffee_item',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
    ]
