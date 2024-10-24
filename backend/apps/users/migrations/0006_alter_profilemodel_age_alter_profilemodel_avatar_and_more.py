# Generated by Django 5.0.6 on 2024-06-10 17:35

import core.services.upload_avatar
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profilemodel_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(15), django.core.validators.MaxValueValidator(130)]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=core.services.upload_avatar.upload_avatar, validators=[django.core.validators.FileExtensionValidator(['gif', 'jpeg', 'png'])]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[A-Z][a-zA-Z]{1,19}$', 'First letter uppercase, min 2 max 20 ch')]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='surname',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[A-Z][a-zA-Z]{1,19}$', 'First letter uppercase, min 2 max 20 ch')]),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=128, validators=[django.core.validators.RegexValidator('^(?=.*\\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\\w\\d\\s:])([^\\s]){8,16}$', ['password must contain 1 number (0-9)', 'password must contain 1 uppercase letters', 'password must contain 1 lowercase letters', 'password must contain 1 non-alpha numeric number', 'password is 8-16 characters with no space'])]),
        ),
    ]
