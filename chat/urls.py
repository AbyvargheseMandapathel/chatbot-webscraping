from django.urls import path
from .views import home, get_response , index
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('home', home, name='home'),
    path('', index, name='index'),
    path('get_response/', get_response, name='get_response'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)