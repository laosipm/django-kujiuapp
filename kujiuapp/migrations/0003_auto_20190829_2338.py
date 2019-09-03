# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kujiuapp', '0002_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='animetype',
        ),
        migrations.DeleteModel(
            name='author',
        ),
        migrations.DeleteModel(
            name='category',
        ),
    ]
