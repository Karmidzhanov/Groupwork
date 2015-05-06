# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20150504_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='meal_description',
            field=models.CharField(max_length=255, verbose_name=b'Menu'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meal',
            name='meal_type',
            field=models.CharField(max_length=2, verbose_name=b'Meal Type', choices=[(b'BF', b'Breakfast'), (b'BN', b'Brunch'), (b'LU', b'Lunch'), (b'DN', b'Dinner')]),
            preserve_default=True,
        ),
    ]
