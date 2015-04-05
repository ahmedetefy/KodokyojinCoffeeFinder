# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0046_page_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee_item',
            name='url',
        ),
        migrations.AddField(
            model_name='coffee_item',
            name='photo',
            field=models.ImageField(default=b'static/images/no-img.jpg', upload_to=b'static/images'),
            preserve_default=True,
        ),
    ]
