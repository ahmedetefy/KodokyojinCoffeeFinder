# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0048_auto_20150404_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='order',
            name='longitude',
        ),
    ]
