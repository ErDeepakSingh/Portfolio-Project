# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-29 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', height_field='300', upload_to='images', width_field='500')),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
    ]
