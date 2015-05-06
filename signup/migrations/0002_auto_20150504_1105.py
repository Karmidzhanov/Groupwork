# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadet',
            name='xNumber',
            field=models.CharField(max_length=6),
            preserve_default=True,
        ),
    ]
