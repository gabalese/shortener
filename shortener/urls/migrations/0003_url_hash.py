# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0002_auto_20150224_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='hash',
            field=models.CharField(default=1, unique=True, max_length=255),
            preserve_default=False,
        ),
    ]
