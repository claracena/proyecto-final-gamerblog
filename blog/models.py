from django.db import models
from django.conf import settings

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name

class Platform(models.Model):
    platform_name = models.CharField(max_length=50)

    def __str__(self):
        return self.platform_name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='post-images/')
    comments = models.IntegerField(default=0, null=True)
    tags = models.ManyToManyField(Tag)
    platforms = models.ManyToManyField(Platform)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.title