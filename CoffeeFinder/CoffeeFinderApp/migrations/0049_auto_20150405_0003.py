# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0048_photomodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='photomodel',
            name='item',
            field=models.ForeignKey(default='', to='CoffeeFinderApp.Coffee_item'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photomodel',
            name='page',
            field=models.ForeignKey(default='', to='CoffeeFinderApp.Page'),
            preserve_default=False,
        ),
    ]
