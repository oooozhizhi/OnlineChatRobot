# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-04 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0004_historymessage_talk_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historymessage',
            name='type',
            field=models.IntegerField(blank=True, default=10000),
        ),
    ]