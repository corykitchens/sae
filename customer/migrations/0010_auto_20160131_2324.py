# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_auto_20160131_1934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['last_name'], 'verbose_name_plural': 'customer'},
        ),
        migrations.AlterModelOptions(
            name='customer_address',
            options={'verbose_name_plural': 'customer_address'},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='middle_initial',
        ),
        migrations.RemoveField(
            model_name='customer_address',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='customer',
            name='cell_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='home_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='customer_address',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.ForeignKey(blank=True, to='customer.Customer_Address', help_text=b'What is the address?', null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(help_text=b'Do they have an Email address?', max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(help_text=b'Their first name', max_length=60),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(help_text=b'Their last name', max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='customer_address',
            name='address',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='customer_address',
            name='city',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='customer_address',
            name='state',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterModelTable(
            name='customer',
            table=None,
        ),
        migrations.AlterModelTable(
            name='customer_address',
            table=None,
        ),
    ]
