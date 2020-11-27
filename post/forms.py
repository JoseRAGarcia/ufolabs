from django.forms import ModelForm
from django import forms
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from .models import Post, PostComment

class CreatePost(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'photo', 'content']


class CommentPost(ModelForm):

    class Meta:
        model = PostComment
        fields = ['content']