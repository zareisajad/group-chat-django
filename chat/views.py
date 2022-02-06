from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    context = {'room_name': room_name, 'username': username}
    return render(request, 'room.html', context)