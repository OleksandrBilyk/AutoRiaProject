# Generated by Django 5.1.2 on 2024-10-25 08:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_carmodel_options_carmodel_body_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='model_car',
            new_name='car_model',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='body_type',
        ),
        migrations.AddField(
            model_name='carmodel',
            name='information',
            field=models.CharField(default=1, max_length=350, validators=[django.core.validators.RegexValidator('^[A-Z][a-zA-Z\\s]{2,349}$', 'first letter uppercase min 3 max 350')]),
            preserve_default=False,
        ),
    ]