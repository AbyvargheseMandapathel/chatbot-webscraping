from django.core.paginator import Paginator
from django.shortcuts import render
from .chatbot import chatbot
from .models import SliderImage, Event, Course , Teachers , Announcements
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


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

def announcements(request):
    announcements_list = Announcements.objects.all().order_by('-date', '-time')
    paginator = Paginator(announcements_list, 10)  # 10 items per page
    page = request.GET.get('page')
    announcements_page = paginator.get_page(page)
    context = {'announcements_page': announcements_page}
    return render(request, 'announcements.html', context)

def teacher_details(request, teacher_id):
    teacher = get_object_or_404(Teachers, pk=teacher_id)
    return render(request, 'teacher_details.html', {'teacher': teacher})



def course_detail(request, course_name):
    course = get_object_or_404(Course, name=course_name)
    return render(request, 'course_details.html', {'course': course})