# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0003_auto_20150426_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like_image',
            name='image',
            field=models.ForeignKey(related_name='likes', to='CoffeeFinderApp.Coffee_page_image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='like_review',
            name='review',
            field=models.ForeignKey(related_name='likes', to='CoffeeFinderApp.Coffee_item_review'),
            preserve_default=True,
        ),
    ]
