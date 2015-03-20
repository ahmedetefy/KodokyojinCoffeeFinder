# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0037_page_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='area',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='city',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='country',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='street_number',
            field=models.IntegerField(default=0, max_length=128),
            preserve_default=False,
        ),
    ]
