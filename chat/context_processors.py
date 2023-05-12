from django.utils import timezone

def timezone_context(request):
    return {'timezone': timezone}
