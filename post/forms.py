from django.forms import ModelForm
from django import forms
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from .models import Post

class CreatePost(ModelForm):

    class Meta:

        model = Post
        fields = ['title', 'photo', 'content']


