# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-11 23:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='todo_element',
            new_name='ToDoElement',
        ),
        migrations.RenameModel(
            old_name='todo_list',
            new_name='ToDoList',
        ),
    ]