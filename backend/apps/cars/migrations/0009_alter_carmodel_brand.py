# Generated by Django 5.1.2 on 2024-11-03 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_alter_currencymodel_buy_alter_currencymodel_ccy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.CharField(choices=[('BMW', 'Bmw'), ('AUDI', 'Audi'), ('Fiat', 'Fiat'), ('Mazda', 'Mazda'), ('Nissan', 'Nissan'), ('Scoda', 'Scoda'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Honda', 'Honda'), ('Hyundai', 'Hyundai'), ('KIA', 'Kia'), ('Lexus', 'Lexus'), ('Mercedes-Benz', 'Mercedes Benz'), ('Mitsubishi', 'Mitsubishi'), ('Opel', 'Opel'), ('Peugeot', 'Peugeot'), ('Toyota', 'Toyota'), ('Volvo', 'Volvo'), ('Volkswagen', 'Volkswagen'), ('Other', 'Other')], max_length=50),
        ),
    ]
