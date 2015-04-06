# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0051_auto_20150406_1910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Name',
            new_name='name',
        ),
    ]
