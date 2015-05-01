# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0002_order2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order2',
            name='Page',
        ),
        migrations.DeleteModel(
            name='Order2',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='coffeeshop',
            new_name='Page',
        ),
        migrations.RemoveField(
            model_name='order',
            name='coffeeshop_item',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='deliveryAddress',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='order',
            field=models.CharField(default=b'', max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='Name',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
    ]
