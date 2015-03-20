# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0004_auto_20150311_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('longitude', models.DecimalField(max_digits=20, decimal_places=10)),
                ('latitude', models.DecimalField(max_digits=20, decimal_places=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
