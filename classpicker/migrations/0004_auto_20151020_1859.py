# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classpicker', '0003_auto_20151020_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pick',
            name='finished',
        ),
        migrations.AddField(
            model_name='pickuser',
            name='finished',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
