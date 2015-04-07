# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0044_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee_page_image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'Coffee_page_images')),
                ('page', models.ForeignKey(to='CoffeeFinderApp.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
