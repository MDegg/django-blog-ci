# Generated by Django 3.2.9 on 2021-12-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_userpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
