# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-07 18:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('workorder', '0006_auto_20160307_1825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workorder',
            old_name='parts_require',
            new_name='parts_required',
        ),
        migrations.AlterField(
            model_name='workorder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 7, 18, 51, 33, 21065, tzinfo=utc)),
        ),
    ]
