# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('user_id', models.BigIntegerField()),
                ('user_name', models.CharField(max_length=255)),
                ('nickname', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=255)),
                ('ts', models.DateTimeField()),
                ('timezone', models.IntegerField()),
                ('ts_japan', models.DateTimeField()),
                ('ts_date_japan', models.DateField()),
                ('tool', models.CharField(max_length=255)),
                ('retweet_cnt', models.IntegerField()),
                ('fav_cnt', models.IntegerField()),
                ('cnt', models.IntegerField()),
                ('link_cnt', models.IntegerField()),
                ('linked_cnt', models.IntegerField()),
                ('listed_cnt', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'timelines',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
