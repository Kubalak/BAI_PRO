# Generated by Django 4.2.4 on 2023-10-27 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='enable_2fa',
            field=models.BooleanField(default=False),
        ),
    ]
