# Generated by Django 5.0.2 on 2024-02-13 11:11

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Polyline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('path', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
        ),
    ]