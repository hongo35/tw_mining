# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FbUser',
            fields=[
                ('user_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'fb_users',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
