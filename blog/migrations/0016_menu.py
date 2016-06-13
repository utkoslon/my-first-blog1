# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20160603_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('items', models.ManyToManyField(to='blog.Post')),
            ],
        ),
    ]
