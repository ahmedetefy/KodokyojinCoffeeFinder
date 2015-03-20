# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0025_auto_20150320_1046'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='coffee_item',
            unique_together=set([('name', 'page')]),
        ),
        migrations.RemoveField(
            model_name='coffee_item',
            name='slug',
        ),
    ]
