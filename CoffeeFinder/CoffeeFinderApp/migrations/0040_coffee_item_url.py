# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0039_auto_20150320_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee_item',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
