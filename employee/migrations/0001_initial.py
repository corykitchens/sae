# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 23:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('middle_initial', models.CharField(max_length=1)),
                ('last_name', models.CharField(max_length=200)),
                ('wage', models.FloatField()),
                ('birthdate', models.DateField()),
                ('sex', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='job_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Job'),
        ),
    ]
