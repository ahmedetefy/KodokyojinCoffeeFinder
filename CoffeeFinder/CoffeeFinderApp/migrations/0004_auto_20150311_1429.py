# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0003_auto_20150311_1411'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CoffeeItem',
            new_name='Coffee_item',
        ),
    ]
