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
    introduction = models.TextField(default='Unknown')
    overview = models.TextField(default='Unknown')
    schedule = models.TextField(default='Unknown')

    def __str__(self):
        return self.name


class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images/')

    def __str__(self):
        return str(self.image)
    
class Course(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='course_images')
    description = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    peo = models.TextField()
    po = models.TextField()
    pso = models.TextField()
    duration = models.CharField(max_length=50, default='Unknown')
    semester = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Teachers(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='teacher_images/')
    designation = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    ug = models.CharField(max_length=255)
    pg = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    experience = models.TextField(default='Unknown')
    qualification = models.TextField(default='Unknown')
    publication = models.TextField(default='Unknown')

    def __str__(self):
        return self.name


