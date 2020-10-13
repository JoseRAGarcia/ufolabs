from django.forms import ModelForm
from django import forms
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from .models import Post

class CreatePost(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user')
    #     super(CreatePost, self).__init__(*args, **kwargs)


    class Meta:

        model = Post
        fields = ['title', 'summary', 'content', 'author']

        widgets = {
            'author': forms.TextInput(attrs={'value': 36}),
        }


