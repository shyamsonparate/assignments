# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-11 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('Email', models.EmailField(help_text=b'A valid email address, please.', max_length=254)),
                ('MobileNo', models.IntegerField(default=0)),
            ],
        ),
    ]
