# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fb_user', '0002_auto_20150218_0242'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FbUser',
        ),
    ]
