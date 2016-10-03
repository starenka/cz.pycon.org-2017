# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-09-29 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0004_auto_20160929_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='level',
            field=models.CharField(choices=[(1, 'Platinum'), (2, 'Gold'), (3, 'Silver'), (4, 'Bronze'), (5, 'Diversity'), (6, 'Media')], default=3, max_length=20),
        ),
    ]