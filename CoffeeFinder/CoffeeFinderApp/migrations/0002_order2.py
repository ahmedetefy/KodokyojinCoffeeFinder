# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.CharField(max_length=500)),
                ('Name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('deliveryAddress', models.CharField(max_length=128)),
                ('Page', models.ForeignKey(to='CoffeeFinderApp.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
