# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-07 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20180907_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='SnippetExtension',
        ),
        migrations.AddField(
            model_name='snippet',
            name='code',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snippetextension',
            name='snippets',
            field=models.ManyToManyField(to='snippets.Snippet'),
        ),
    ]
