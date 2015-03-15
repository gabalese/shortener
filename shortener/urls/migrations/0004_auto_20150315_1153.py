# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0003_url_hash'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='url',
            new_name='original_url',
        ),
    ]
