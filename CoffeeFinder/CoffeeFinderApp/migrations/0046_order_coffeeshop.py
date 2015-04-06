# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0045_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coffeeshop',
            field=models.ForeignKey(default=0, to='CoffeeFinderApp.Page'),
            preserve_default=False,
        ),
    ]
