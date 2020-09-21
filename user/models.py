# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class My_User(User):
    photo = models.ImageField(upload_to='user_photos', null=True, blank=True)

    def __unicode__(self):
        return self.username