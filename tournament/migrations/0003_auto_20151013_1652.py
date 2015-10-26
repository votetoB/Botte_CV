# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_auto_20151011_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(related_name='winner', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
