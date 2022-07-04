# Generated by Django 4.0.6 on 2022-07-04 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_usermodel_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='password',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='first_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
