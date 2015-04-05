# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0044_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
                ('Name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('coffeeshop_item', models.ForeignKey(to='CoffeeFinderApp.Coffee_item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
