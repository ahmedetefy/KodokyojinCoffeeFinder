# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0022_auto_20150320_1043'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='coffee_item',
            unique_together=set([('name', 'slug', 'page')]),
        ),
    ]
