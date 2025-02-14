# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 21:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle', '0001_initial'),
        ('customer', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeServiceNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_serviced', models.DateTimeField()),
                ('hours_spent', models.FloatField()),
                ('notes', models.CharField(max_length=400)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odometer', models.IntegerField()),
                ('date_created', models.DateTimeField(default=datetime.datetime(2016, 3, 9, 21, 17, 12, 323465, tzinfo=utc))),
                ('problem_description', models.CharField(max_length=400)),
                ('estimate_initial', models.FloatField(blank=True)),
                ('estimate_revision', models.FloatField(blank=True, null=True)),
                ('hours_required', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Assigned', 'Assigned'), ('Diagnosing', 'Diagnosing'), ('Repairing', 'Repairing'), ('Reassigned', 'Reassigned'), ('Completed', 'Completed'), ('Awaiting Payment', 'Awaiting Payment'), ('Paid in Full', 'Paid in Full'), ('Closed', 'Closed'), ('Cancelled', 'Cancelled')], max_length=100, null=True)),
                ('parts_required', models.CharField(blank=True, max_length=200, null=True)),
                ('estimate_approval', models.NullBooleanField()),
                ('approval_date_time', models.DateTimeField(blank=True, null=True)),
                ('amount_paid', models.FloatField(blank=True, null=True)),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
                ('service_type', models.ManyToManyField(to='workorder.ServiceType')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Vehicle')),
            ],
            options={
                'db_table': 'CKTM_WORKORDER',
            },
        ),
        migrations.AddField(
            model_name='employeeservicenotes',
            name='parts_used',
            field=models.ManyToManyField(blank=True, null=True, to='workorder.Part'),
        ),
        migrations.AddField(
            model_name='employeeservicenotes',
            name='work_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workorder.WorkOrder'),
        ),
    ]
