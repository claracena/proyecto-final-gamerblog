from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    comments = models.IntegerField(default=0)
    category = models.CharField(max_length=255)
    # author = models.OneToOneField('account.Account', on_delete=models.CASCADE)


    def __str__(self):
        return self.title