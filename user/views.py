from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import My_User
from .forms import CreateUser, UpdateUser
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

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user':user})

@login_required
def update_user(request, id):
    user = get_object_or_404(My_User, pk=id)
    form = UpdateUser(request.POST or None, request.FILES or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'userUpdate.html', {'form': form})