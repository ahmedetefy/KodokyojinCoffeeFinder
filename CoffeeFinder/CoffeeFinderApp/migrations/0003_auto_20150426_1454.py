# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CoffeeFinderApp', '0002_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like_Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('image', models.ForeignKey(to='CoffeeFinderApp.Coffee_page_image')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like_Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('review', models.ForeignKey(to='CoffeeFinderApp.Coffee_item_review')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='like',
            name='page_image',
        ),
        migrations.RemoveField(
            model_name='like',
            name='review',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
