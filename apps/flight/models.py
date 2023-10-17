from django.db.models import *

from apps.airline.models import Airline
from apps.plane.models import Plane

class Flight(Model):

    from_place = CharField(
        verbose_name='Откуда',
        max_length=256
    )
    to_place = CharField(
        verbose_name='Куда',
        max_length=256
    )
    plane = ForeignKey(
        Plane,
        on_delete=CASCADE,
        verbose_name='Самолет рейса'
    )
    airline = ForeignKey(
        Airline,
        on_delete=CASCADE,
        verbose_name='Аэропорт рейса'
    )
    price = DecimalField(
        verbose_name='Цена билета',
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.id}'
