from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import My_User, Relationship
from post.models import Post
from .forms import CreateUser, UpdateUser
from django.contrib import messages
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
    frequest = Relationship.objects.filter(to_user=request.user)
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'profile.html', {'user':user, 'posts': posts, 'frequest': frequest})

@login_required
def person(request, id):
    posts = Post.objects.all()
    user_posts = Post.objects.filter(author=id).order_by('-created_at')
    user = get_object_or_404(My_User, pk=id)
    users = My_User.objects.all()
    friend = My_User.objects.filter(friends=request.user)

    return render(request, 'person.html', {'user': user, 'posts': posts, 'user_posts': user_posts, 'users': users, 'friend': friend})

@login_required
def update_user(request, id):
    user = get_object_or_404(My_User, pk=id)
    form = UpdateUser(request.POST or None, request.FILES or None, instance=user)

    if form.is_valid():
        form.save()
        messages.info(request, "Dados deste ser alterados com sucesso! (Sua foto de perfil pode levar até 24hrs para ser aprovada)")
        return redirect('profile')

    return render(request, 'userUpdate.html', {'form': form})

def add_friend(request, id):
    from_user = request.user
    to_user = My_User.objects.get(id=id)
    frequest = Relationship.objects.get_or_create(from_user=from_user, to_user=to_user)
    messages.info(request, "Tentativa de abdução realizada com sucesso!")
    return redirect('profile')

def accept_friend(request, id):
    frequest = Relationship.objects.get(id=id)
    user1 = request.user
    user2 = frequest.from_user
    user1.friends.add(user2.id)
    user2.friends.add(user1.id)
    frequest.delete()
    messages.info(request, f"{user2.first_name} conseguiu te abduzir com sucesso!")
    return redirect('profile')

def requests_page(request, id):
    frequest = Relationship.objects.filter(to_user=request.user)
    return render(request, 'requests_page.html', {'frequest': frequest})