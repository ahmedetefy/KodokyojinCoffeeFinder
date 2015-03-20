# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0029_auto_20150320_1049'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='coffee_item',
            unique_together=set([]),
        ),
    ]
