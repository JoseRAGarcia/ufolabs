from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import CreatePost
from django.views.generic.edit import UpdateView

# Create your views here.

def home(request):
    posts = Post.objects.all()
    user = request.user
    return render(request, 'home.html', {'posts': posts, 'user': user})

@login_required
def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post.html', {'post': post})

@login_required
def new_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CreatePost()
    return render(request, 'postCreation.html', {'form':form})

# class MyUpdateView(UpdateView):
#
#     model = Post
#     form_class = CreatePost
#
#     # Sending user object to the form, to verify which fields to display/remove (depending on group)
#     def get_form_kwargs(self):
#         kwargs = super(MyUpdateView, self).get_form_kwargs()
#         kwargs.update({'user': self.request.user})
#         return kwargs