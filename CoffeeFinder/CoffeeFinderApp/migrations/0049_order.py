# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0048_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
                ('Name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('status', models.CharField(max_length=128)),
                ('coffeeshop', models.ForeignKey(to='CoffeeFinderApp.Page')),
                ('coffeeshop_item', models.ForeignKey(to='CoffeeFinderApp.Coffee_item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
