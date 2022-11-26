# Generated by Django 4.0.5 on 2022-11-25 20:32

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_tinder', '0006_customuser_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326),
        ),
    ]
