# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0051_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coffeeshop',
            field=models.ForeignKey(default=0, to='CoffeeFinderApp.Page'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='pending', max_length=128),
            preserve_default=False,
        ),
    ]
