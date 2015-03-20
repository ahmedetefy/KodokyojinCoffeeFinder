# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0011_auto_20150320_0950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='slu',
            new_name='slug',
        ),
    ]
