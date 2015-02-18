# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fb_user', '0003_delete_fbuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='FbUsers',
            fields=[
                ('user_id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=255)),
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
