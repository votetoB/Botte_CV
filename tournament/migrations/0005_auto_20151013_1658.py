# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_auto_20151013_1655'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together=set([('tournament', 'user')]),
        ),
    ]
