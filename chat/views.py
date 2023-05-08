from django.shortcuts import render
from .chatbot import chatbot

from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')
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
