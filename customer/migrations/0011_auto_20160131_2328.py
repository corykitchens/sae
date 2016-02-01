# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_auto_20160131_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='middle_initial',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='customer_address',
            name='zip_code',
            field=models.IntegerField(default=93313),
        ),
    ]
