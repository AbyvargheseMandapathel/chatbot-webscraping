from django.urls import path
from .views import home, get_response , index , courses , events , teachers
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('index', index, name='index'),
    path('courses', courses, name='courses'),
    path('events', events, name='events'),
    path('teachers', teachers, name='teachers'),
    path('get_response/', get_response, name='get_response'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
