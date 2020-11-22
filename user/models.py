# -*- coding: utf-8 -*-
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class My_User(User):
    photo = models.ImageField(upload_to='user_photos', null=True, blank=True)
    bio = RichTextField(blank=True)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)

    def get_friends(self):
        return self.friends.all()

    def get_friends_number(self):
        return self.friends.all().count()

    def __unicode__(self):
        return self.username

class Relationship(models.Model):
    from_user  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user', null=True)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user', null=True)

