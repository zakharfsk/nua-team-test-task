# Generated by Django 4.0.6 on 2022-07-04 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_usermodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='user_id',
            field=models.IntegerField(blank=True, default=2),
            preserve_default=False,
        ),
    ]