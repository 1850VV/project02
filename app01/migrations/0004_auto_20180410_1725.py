# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20180410_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee2',
            old_name='salary',
            new_name='salary2',
        ),
    ]
