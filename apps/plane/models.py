from django.db.models import *

class Plane(Model):

    name = CharField(
        verbose_name='Название самолета',
        max_length=256
    )
    characteristics = TextField(
        verbose_name='Характеристики',
        blank=True,
        null=True
    )
    capacity = IntegerField(
        verbose_name='Вместимость'
    )

    def __str__(self):
        return f'{self.name}'