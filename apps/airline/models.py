from django.db.models import *

from apps.plane.models import Plane

class Airline(Model):

    name = CharField(
        verbose_name='Имя аэропорта',
        max_length=256
    )
    created_at = DateField(
        verbose_name='Основан в'
    )
    planes = ForeignKey(
        Plane,
        on_delete=CASCADE,
        verbose_name='Самолеты аэропорта'
    )

    def __str__(self):
        return f'{self.name}'


