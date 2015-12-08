# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0015_auto_20151106_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='author_left',
            field=models.CharField(max_length=255, help_text='author who has left Choimirai', blank=True),
        ),
        migrations.AlterField(
            model_name='workpage',
            name='author_left',
            field=models.CharField(max_length=255, help_text='author who has left Choimirai', blank=True),
        ),
    ]
