from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, PostComment
from .forms import CreatePost, CommentPost
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic.edit import UpdateView

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    user = request.user
    return render(request, 'home.html', {'posts': posts, 'user': user})

@login_required
def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = CommentPost(request.POST or None)
    comments = PostComment.objects.all().filter(post=post_id)
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        liked = True

    return render(request, 'post.html', {'post': post, 'liked': liked, 'form': form, 'comments': comments})

@login_required
def new_post(request):
    if request.method == 'POST':
        item = Post(author=request.user)
        form = CreatePost(request.POST or None, request.FILES or None, instance=item)

        if form.is_valid():
            form.save()
            messages.info(request, "Mensagem enviada ao Espaço com sucesso! (A sua postagem pode levar até 24hrs para ser aprovada)")
            return redirect('profile')
    else:
        form = CreatePost()

    return render(request, 'postCreation.html', {'form':form})

def like_post(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post', args=[str(pk)]))

@login_required
@user_passes_test(lambda u: u.is_superuser)
def allow_post(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('allow_post_id'))
    post.online = True
    post.save()
    messages.info(request, "Postagem aprovada com sucesso. Agora ela é pública")
    return redirect('profile')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

def comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        item = PostComment(author=request.user, post=post)
        form = CommentPost(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            #messages.info(request, "Mensagem enviada ao Espaço com sucesso! (A sua postagem pode levar até 24hrs para ser aprovada)")
            return HttpResponseRedirect(reverse('post', args=[str(post_id)]))
