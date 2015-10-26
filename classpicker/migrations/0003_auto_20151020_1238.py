# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classpicker', '0002_auto_20151020_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hearthstoneclass',
            name='title',
            field=models.CharField(max_length=7),
            preserve_default=True,
        ),
    ]
