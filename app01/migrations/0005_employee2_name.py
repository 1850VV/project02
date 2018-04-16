# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20180410_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee2',
            name='name',
            field=models.CharField(max_length=20, default='hh'),
        ),
    ]
