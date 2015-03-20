# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0010_page_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='slug',
            new_name='slu',
        ),
    ]
