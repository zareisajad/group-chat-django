from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import UserRegistrationForm, UserLoginForm
from .models import User


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            check_user = User.objects.filter(username=data['username'])
            if not check_user:
                user = User.objects.create_user(
                    data['username'], data['password']
                )
                return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'], password=data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('chat:index')
            else:
                return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('accounts:login')
