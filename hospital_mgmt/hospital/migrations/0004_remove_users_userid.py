# Generated by Django 4.1.3 on 2022-12-09 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_users_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='userid',
        ),
    ]
