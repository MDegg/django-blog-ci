# Generated by Django 3.2.9 on 2021-12-23 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0004_auto_20211223_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpost',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='userpost',
            name='status',
        ),
    ]
