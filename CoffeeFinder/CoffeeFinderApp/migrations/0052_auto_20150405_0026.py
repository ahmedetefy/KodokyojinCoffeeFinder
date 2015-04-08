# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0051_coffee_page_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coffee_page_image',
            new_name='Coffee_item_image',
        ),
    ]
