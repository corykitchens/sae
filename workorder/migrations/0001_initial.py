# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_auto_20160130_2154'),
        ('customer', '0011_auto_20160131_2328'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('odometer', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('problem_description', models.CharField(max_length=400)),
                ('estimate_initial', models.IntegerField(blank=True)),
                ('estimate_revision', models.FloatField(blank=True)),
                ('hours_required', models.FloatField()),
                ('parts_require', models.CharField(max_length=200, blank=True)),
                ('estimate_approval', models.CharField(max_length=100, blank=True)),
                ('approval_date_time', models.DateTimeField(blank=True)),
                ('amount_paid', models.FloatField(blank=True)),
                ('date_completed', models.DateTimeField(blank=True)),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('employee', models.ForeignKey(to='employee.Employee')),
                ('service_type', models.ManyToManyField(to='workorder.ServiceType')),
                ('vehicle', models.ForeignKey(to='vehicle.Vehicle')),
            ],
            options={
                'db_table': 'CKTM_WORKORDER',
            },
        ),
    ]
