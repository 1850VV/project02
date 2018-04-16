# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('create_date', models.DateField()),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField(default=0)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comment', models.CharField(max_length=500)),
                ('department', models.ForeignKey(to='app01.Department')),
            ],
        ),
    ]
