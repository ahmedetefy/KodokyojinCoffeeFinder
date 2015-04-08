# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0045_coffee_item_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffee_item_review',
            old_name='coffee_item_id',
            new_name='coffee_item',
        ),
        migrations.RenameField(
            model_name='coffee_item_review',
            old_name='user_id',
            new_name='user',
        ),
    ]
