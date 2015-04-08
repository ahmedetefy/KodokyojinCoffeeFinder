# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0049_auto_20150405_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photomodel',
            name='item',
        ),
        migrations.RemoveField(
            model_name='photomodel',
            name='page',
        ),
        migrations.DeleteModel(
            name='PhotoModel',
        ),
    ]
