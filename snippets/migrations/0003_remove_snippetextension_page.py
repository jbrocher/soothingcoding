# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-07 07:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_snippetextension_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippetextension',
            name='page',
        ),
    ]
