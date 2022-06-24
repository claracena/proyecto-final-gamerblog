from django.db import models
from django.conf import settings
from django.urls import reverse
from ckeditor.fields import RichTextField

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
    body = RichTextField()
    image = models.ImageField(blank=True, null=True, upload_to='post-images/')
    comments = models.IntegerField(default=0, null=True)
    tags = models.ManyToManyField(Tag)
    platforms = models.ManyToManyField(Platform)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        # return reverse('article', args=(str(self.id)))
        return reverse('blog')

class Comment(models.Model):
    # email = models.CharField(max_length=150, null=False)
    # name = models.CharField(max_length=150, null=False)
    # website = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=False)
    comment_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, related_name='articles', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comment_author', verbose_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author) + " - " + str(self.blog) + " - " + str(self.message)
