# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='comment',
            field=models.TextField(max_length=1000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='current_participants',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
