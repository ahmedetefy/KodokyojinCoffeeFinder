# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0047_auto_20150404_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model_pic', models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'pic_folder/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
