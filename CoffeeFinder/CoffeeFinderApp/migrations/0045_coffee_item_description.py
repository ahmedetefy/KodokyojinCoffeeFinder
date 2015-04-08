# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0044_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee_item',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
