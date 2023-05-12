from django import forms
from .models import Event, SliderImage

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_description', 'event_image', 'ticket_fee', 'event_date', 'start_time', 'end_time', 'event_location', 'seating_capacity']

class SliderImageForm(forms.ModelForm):
    class Meta:
        model = SliderImage
        fields = ['image']
