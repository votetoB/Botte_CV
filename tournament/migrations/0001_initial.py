# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.PositiveIntegerField()),
                ('left_user', models.ForeignKey(related_name='left_user', blank=True, to=settings.AUTH_USER_MODEL)),
                ('right_user', models.ForeignKey(related_name='right_user', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200)),
                ('start_time', models.DateTimeField()),
                ('max_participants', models.PositiveIntegerField()),
                ('current_participants', models.PositiveIntegerField()),
                ('comment', models.TextField(max_length=1000)),
                ('has_started', models.BooleanField(default=False)),
                ('has_ended', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='registration',
            name='tournament',
            field=models.ForeignKey(to='tournament.Tournament'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registration',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(to='tournament.Tournament'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(related_name='winner', blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
