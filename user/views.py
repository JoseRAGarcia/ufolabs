from django.shortcuts import render, redirect, get_object_or_404
from .models import My_User
from .forms import CreateUser
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUser()

    return render(request, 'registro.html', {'form':form})

def profile(request):
    users = request.user
    return render(request, 'profile.html', {'users':users})