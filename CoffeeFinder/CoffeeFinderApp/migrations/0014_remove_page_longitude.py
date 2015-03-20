# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0013_remove_page_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='longitude',
        ),
    ]
