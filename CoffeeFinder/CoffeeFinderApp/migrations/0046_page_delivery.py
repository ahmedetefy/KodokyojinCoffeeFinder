# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0045_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='delivery',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
