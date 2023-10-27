from django.db import models

class City(models.Model):

    name = models.CharField(max_length=100, unique=True, verbose_name="Название города")

    def __str__(self):
        return self.name


class Car(models.Model):

    make = models.CharField(max_length=50, verbose_name="Марка")
    model = models.CharField(max_length=50, verbose_name="Модель")
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    registration_number = models.CharField(max_length=20, verbose_name="Регистрационный номер")
    color = models.CharField(max_length=30, verbose_name="Цвет")
    range = models.PositiveIntegerField(verbose_name="Запас хода")
    is_available = models.BooleanField(default=True, verbose_name="Доступен для аренды")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Город")

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
