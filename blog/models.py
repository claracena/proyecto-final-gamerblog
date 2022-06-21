from django.db import models
from django.conf import settings

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='post-images/')
    comments = models.IntegerField(default=0, null=True)
    category = models.CharField(max_length=255)
    platform = models.CharField(max_length=255, default='all')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.title