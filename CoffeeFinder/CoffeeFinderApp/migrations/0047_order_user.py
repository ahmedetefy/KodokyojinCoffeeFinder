# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0046_order_coffeeshop'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.CharField(default=0, max_length=128),
            preserve_default=False,
        ),
    ]
