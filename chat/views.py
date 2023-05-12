from django.shortcuts import render
from .chatbot import chatbot
from .models import SliderImage, Event

from django.http import HttpResponse

def home(request):
    sliders = SliderImage.objects.all()
    events = Event.objects.all()
    return render(request, 'index.html', {'sliders': sliders, 'events': events})

def index(request):
    return render(request, 'home.html')

def get_response(request):
    if request.method == 'GET':
        message = request.GET.get('message')
        if message:
            response = chatbot(request, message)
            return HttpResponse(response)
        else:
            return HttpResponse('Please provide a message')
    else:
        return HttpResponse('Invalid request method')
