from django.contrib import admin
from .models import SliderImage, Event, Course, Teachers

@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ['image']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'ticket_fee', 'date', 'start_time', 'end_time', 'place', 'seat']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']

    fieldsets = (
        (None, {'fields': ('name', 'image')}),
        ('Course Details', {'fields': ('duration', 'semester')}),
        ('Description', {'fields': ('description',)}),
        ('Program Info', {'fields': ('mission', 'vision', 'peo', 'po', 'pso')}),
    )

    # Override save method to handle uploaded image
    def save_model(self, request, obj, form, change):
        if 'image' in form.cleaned_data:
            obj.image = form.cleaned_data['image']
        super().save_model(request, obj, form, change)
        

admin.site.register(Teachers)

