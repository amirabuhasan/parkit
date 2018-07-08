# Generated by Django 2.0.4 on 2018-07-06 07:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(default='None', max_length=100)),
                ('car_registery', models.CharField(default='ABC1234', max_length=100)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('parked_at', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rent.ParkingForRent')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
