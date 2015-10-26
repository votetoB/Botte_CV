# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HearthstoneClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=7)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('finished', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PickUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('battle_tag', models.CharField(max_length=100)),
                ('choices', models.ManyToManyField(to='classpicker.HearthstoneClass')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pick',
            name='first_user',
            field=models.ForeignKey(related_name='first_user', to='classpicker.PickUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pick',
            name='second_user',
            field=models.ForeignKey(related_name='second_user', to='classpicker.PickUser'),
            preserve_default=True,
        ),
    ]
