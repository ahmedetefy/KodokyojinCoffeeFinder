# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0031_auto_20150320_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee_item',
            name='slug',
        ),
    ]
