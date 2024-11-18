# Generated by Django 5.1.3 on 2024-11-17 17:17

import core.services.upload_photo_car
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_carmodel_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='photo_car',
        ),
        migrations.CreateModel(
            name='CarPhotoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(blank=True, upload_to=core.services.upload_photo_car.upload_photo_car, validators=[django.core.validators.FileExtensionValidator(['gif', 'jpeg', 'png'])])),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_car', to='cars.carmodel')),
            ],
            options={
                'db_table': 'car_photos',
            },
        ),
    ]