# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-23 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0158_realm_video_chat_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='realm',
            name='google_hangouts_domain',
            field=models.TextField(default=''),
        ),
    ]
