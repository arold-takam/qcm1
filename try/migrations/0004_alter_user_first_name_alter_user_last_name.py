# Generated by Django 4.2.11 on 2024-12-19 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('try', '0003_remove_user_confirm_password_remove_user_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
