# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_auto_20151013_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='left_user',
            field=models.ForeignKey(related_name='left_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='match',
            name='right_user',
            field=models.ForeignKey(related_name='right_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(related_name='winner', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='comment',
            field=models.TextField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
