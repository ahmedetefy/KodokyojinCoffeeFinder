# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='verified',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
    ]
