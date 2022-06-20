from django.urls import path
from blog.views import blog

urlpatterns = [
    path('', blog, name='blog'),
]