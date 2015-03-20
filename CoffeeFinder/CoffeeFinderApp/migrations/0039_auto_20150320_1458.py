# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0038_auto_20150320_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='area',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='city',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='country',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='street_number',
            field=models.IntegerField(default=0, max_length=12),
            preserve_default=True,
        ),
    ]
