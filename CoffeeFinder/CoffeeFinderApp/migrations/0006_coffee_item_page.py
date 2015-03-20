# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0005_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee_item',
            name='page',
            field=models.ForeignKey(default=0, to='CoffeeFinderApp.Page'),
            preserve_default=True,
        ),
    ]
