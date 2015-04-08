# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee_item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('price', models.IntegerField(default=0)),
                ('slug', models.SlugField()),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coffee_item_image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'Coffee_item_images')),
                ('item', models.ForeignKey(to='CoffeeFinderApp.Coffee_item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coffee_item_review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field', models.TextField(max_length=400)),
                ('coffee_item', models.ForeignKey(to='CoffeeFinderApp.Coffee_item')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coffee_page_image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'Coffee_page_images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
                ('Name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('status', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=128)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('longitude', models.DecimalField(default=0.0, max_digits=50, decimal_places=30)),
                ('latitude', models.DecimalField(default=0.0, max_digits=50, decimal_places=30)),
                ('slug', models.SlugField(unique=True)),
                ('delivery', models.BooleanField(default=False)),
                ('area', models.CharField(default=b'', max_length=128)),
                ('city', models.CharField(default=b'', max_length=128)),
                ('country', models.CharField(default=b'', max_length=128)),
                ('street_number', models.CharField(default=0, max_length=12)),
                ('description', models.CharField(default=b'', max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='coffeeshop',
            field=models.ForeignKey(to='CoffeeFinderApp.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='coffeeshop_item',
            field=models.ForeignKey(to='CoffeeFinderApp.Coffee_item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coffee_page_image',
            name='page',
            field=models.ForeignKey(to='CoffeeFinderApp.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coffee_page_image',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coffee_item_image',
            name='page',
            field=models.ForeignKey(to='CoffeeFinderApp.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coffee_item',
            name='page',
            field=models.ForeignKey(to='CoffeeFinderApp.Page'),
            preserve_default=True,
        ),
    ]
