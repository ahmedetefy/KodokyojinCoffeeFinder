# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0003_administrator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrator',
            name='user',
        ),
        migrations.DeleteModel(
            name='Administrator',
        ),
    ]
