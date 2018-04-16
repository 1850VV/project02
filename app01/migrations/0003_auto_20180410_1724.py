# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_employee2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee2',
            old_name='name',
            new_name='name2',
        ),
    ]
