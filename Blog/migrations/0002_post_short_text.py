# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_text',
            field=models.CharField(default='Short text, where says what about this post', max_length=600),
            preserve_default=False,
        ),
    ]