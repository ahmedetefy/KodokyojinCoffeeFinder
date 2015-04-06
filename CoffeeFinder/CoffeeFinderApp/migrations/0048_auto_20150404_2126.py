# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0047_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='latitude',
            field=models.DecimalField(default=0.0, max_digits=50, decimal_places=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='longitude',
            field=models.DecimalField(default=0.0, max_digits=50, decimal_places=30),
            preserve_default=True,
        ),
    ]
