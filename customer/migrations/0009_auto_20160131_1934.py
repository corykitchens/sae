# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20160131_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.ForeignKey(blank=True, to='customer.Customer_Address', null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=200, unique=True, null=True, blank=True),
        ),
    ]
