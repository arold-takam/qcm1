# Generated by Django 4.2.11 on 2024-12-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('try', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='username', max_length=50),
        ),
    ]
