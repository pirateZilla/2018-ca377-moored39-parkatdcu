# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 18:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('campus', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Carpark',
            fields=[
                ('carpark', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('opening_hours', models.TimeField()),
                ('closing_hours', models.TimeField()),
                ('spaces', models.IntegerField()),
                ('disabled_spaces', models.IntegerField()),
                ('entrance_location', models.CharField(max_length=50)),
                ('is_free', models.BooleanField()),
                ('is_for_public', models.BooleanField()),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='park_at_dcu.Campus')),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('facility_id', models.IntegerField(primary_key=True, serialize=False)),
                ('facility_name', models.CharField(max_length=100)),
                ('carpark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='park_at_dcu.Carpark')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalData',
            fields=[
                ('data_id', models.IntegerField(primary_key=True, serialize=False)),
                ('week', models.IntegerField()),
                ('am7', models.CharField(max_length=10)),
                ('am8', models.CharField(max_length=10)),
                ('am9', models.CharField(max_length=10)),
                ('am10', models.CharField(max_length=10)),
                ('am11', models.CharField(max_length=10)),
                ('pm12', models.CharField(max_length=10)),
                ('pm13', models.CharField(max_length=10)),
                ('pm14', models.CharField(max_length=10)),
                ('pm15', models.CharField(max_length=10)),
                ('pm16', models.CharField(max_length=10)),
                ('pm17', models.CharField(max_length=10)),
                ('pm18', models.CharField(max_length=10)),
                ('pm19', models.CharField(max_length=10)),
                ('pm20', models.CharField(max_length=10)),
                ('pm21', models.CharField(max_length=10)),
                ('carpark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='park_at_dcu.Carpark')),
            ],
        ),
    ]
