from django.db import models

from apps.cars.models import CarModel


class CarViewingModel(models.Model):
    class Meta:
        db_table = 'car_viewing'
    created_at = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='car_view')
