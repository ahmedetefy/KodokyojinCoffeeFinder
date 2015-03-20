# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0002_auto_20150311_1334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffeeitem',
            old_name='title',
            new_name='name',
        ),
    ]
