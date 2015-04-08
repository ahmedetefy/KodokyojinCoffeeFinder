# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0050_auto_20150405_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee_page_image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'Coffee_item_images')),
                ('item', models.ForeignKey(to='CoffeeFinderApp.Coffee_item')),
                ('page', models.ForeignKey(to='CoffeeFinderApp.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
