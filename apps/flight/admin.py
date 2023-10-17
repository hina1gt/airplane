from django.contrib.admin import *

from .models import Flight

@register(Flight)
class AirlineAdmin(ModelAdmin):

    list_display = ('id',)
    list_display_links = ('id',)

