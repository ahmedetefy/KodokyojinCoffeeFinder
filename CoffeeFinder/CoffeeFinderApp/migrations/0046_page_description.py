# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0045_coffee_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='description',
            field=models.CharField(default=b'', max_length=500),
            preserve_default=True,
        ),
    ]
