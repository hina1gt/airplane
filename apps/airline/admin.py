from django.contrib.admin import *

from .models import Airline

@register(Airline)
class AirlineAdmin(ModelAdmin):

    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
