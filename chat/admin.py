from django.contrib import admin
from .models import SliderImage, Event

@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ['image']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'ticket_fee', 'date', 'start_time', 'end_time', 'place', 'seat']
