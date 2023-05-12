from django.core.paginator import Paginator
from django.shortcuts import render
from .chatbot import chatbot
from .models import SliderImage, Event, Course , Teachers
from django.http import HttpResponse

def home(request):
    sliders = SliderImage.objects.all()
    events = Event.objects.all()
    courses = Course.objects.all()
    return render(request, 'index.html', {'sliders': sliders, 'events': events, 'courses': courses})

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

def courses(request):
    courses = Course.objects.all()
    paginator = Paginator(courses, 9) # Show 9 courses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'courses.html', {'courses': page_obj})

def events(request):
    event_list = Event.objects.all()
    paginator = Paginator(event_list, 3) # 3 events per page
    page = request.GET.get('page')
    events = paginator.get_page(page)
    return render(request, 'event.html', {'events': events})

def teachers(request):
    teachers_list = Teachers.objects.all()
    paginator = Paginator(teachers_list, 10) # Show 10 teachers per page
    page = request.GET.get('page')
    teachers = paginator.get_page(page)
    return render(request, 'teachers.html', {'teachers': teachers})
