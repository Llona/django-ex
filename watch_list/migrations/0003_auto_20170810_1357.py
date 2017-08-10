# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('watch_list', '0002_auto_20170809_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 10, 13, 57, 51, 656781), null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 10, 13, 57, 51, 656781), null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='url',
            field=models.CharField(max_length=350, blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 10, 13, 57, 51, 659781)),
        ),
        migrations.AlterField(
            model_name='watchstate',
            name='watch_last_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 10, 13, 57, 51, 658781), null=True),
        ),
    ]
