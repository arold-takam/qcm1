# Generated by Django 4.2.11 on 2024-12-19 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('try', '0002_user_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirm_password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
    ]