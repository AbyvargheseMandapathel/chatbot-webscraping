from django.urls import path
from .views import home, get_response , index , courses , events , teachers ,announcements
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('index', index, name='index'),
    path('courses', courses, name='courses'),
    path('events', events, name='events'),
    path('teachers', teachers, name='teachers'),
    path('announcements', announcements, name='announcements'),
    path('get_response/', get_response, name='get_response'),
    path('teacher/<int:teacher_id>/', views.teacher_details, name='teacher_details'),
    path('course/<str:course_name>/', views.course_detail, name='course_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
