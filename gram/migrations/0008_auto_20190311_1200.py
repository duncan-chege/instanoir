# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-11 09:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0007_auto_20190310_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='username',
        ),
    ]