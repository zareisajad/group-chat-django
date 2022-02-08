from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Message


def index(request):
    return render(request, 'index.html')


@login_required
def room(request, room_name):
    messages = Message.objects.filter(room=room_name).all()
    context = {
        'room_name': room_name,
        'username': request.user.username,
        'messages':messages
    }
    return render(request, 'room.html', context)