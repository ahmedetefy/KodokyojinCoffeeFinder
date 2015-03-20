# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0018_auto_20150320_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee_item',
            name='page',
            field=models.ForeignKey(to='CoffeeFinderApp.Page', unique=True),
            preserve_default=True,
        ),
    ]
