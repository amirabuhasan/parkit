# Generated by Django 2.0.4 on 2018-05-31 10:25

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='user',
            name='image_width',
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_location),
        ),
    ]
