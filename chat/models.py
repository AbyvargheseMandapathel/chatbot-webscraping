from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/')
    ticket_fee = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    place = models.CharField(max_length=255)
    seat = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images/')

    def __str__(self):
        return str(self.image)
