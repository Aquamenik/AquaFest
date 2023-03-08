from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Nie ma takiego użytkownika')

    context = {}
    return render(request, 'login_register.html')


def home(request):
    return render(request, 'home.html')



