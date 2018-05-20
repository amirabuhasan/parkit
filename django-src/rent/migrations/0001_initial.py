# Generated by Django 2.0.4 on 2018-05-20 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingForRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_property', models.TextField(default='Property Name')),
                ('db_address', models.TextField(default='Address')),
                ('db_longitude', models.CharField(default='Longitude', max_length=255)),
                ('db_latitude', models.CharField(default='Latitude', max_length=255)),
                ('db_area', models.CharField(blank=True, max_length=200)),
                ('db_bay', models.CharField(default='Please Update Bay #', max_length=100)),
                ('db_type', models.CharField(default='Type of Building', max_length=100)),
                ('db_reserved', models.CharField(default='Yes', max_length=3)),
                ('db_period', models.CharField(blank=True, max_length=100)),
                ('db_price', models.CharField(blank=True, max_length=100)),
                ('db_sale_price', models.CharField(blank=True, max_length=100)),
                ('db_status', models.CharField(choices=[('Approved', 'Approved'), ('Occupied', 'Occupied'), ('Pending', 'Pending')], default='Pending', max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('serial_no', models.CharField(blank=True, max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
