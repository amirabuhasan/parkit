# Generated by Django 2.0.4 on 2018-05-19 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20180424_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='parked_bay',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='parked_condo',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]