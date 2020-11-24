from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='post_photos', null=True, blank=True)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    online = models.BooleanField(default=False)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


