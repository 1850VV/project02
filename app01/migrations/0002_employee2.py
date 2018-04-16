# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField(default=0)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comment', models.CharField(max_length=500)),
                ('department', models.ForeignKey(to='app01.Department')),
            ],
        ),
    ]
