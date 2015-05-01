# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0002_auto_20150429_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='owner',
            field=models.CharField(unique=True, max_length=128),
            preserve_default=True,
        ),
    ]
