# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classpicker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hearthstoneclass',
            name='title',
            field=models.CharField(max_length=7, verbose_name=b'bla'),
            preserve_default=True,
        ),
    ]
