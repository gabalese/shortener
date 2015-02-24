# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.URLField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
