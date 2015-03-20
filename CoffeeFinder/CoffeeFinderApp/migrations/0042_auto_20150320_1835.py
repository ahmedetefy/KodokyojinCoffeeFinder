# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0041_page_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='street_number',
            field=models.CharField(default=0, max_length=12),
            preserve_default=True,
        ),
    ]
