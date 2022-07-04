from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Головна сторінка',
        'user': request.user,
        'admins': User.objects.filter(is_superuser=True),
    }
    return render(request, 'home_page/index.html', context)
