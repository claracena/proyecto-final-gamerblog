from django.urls import path
from blog.views import blog, post_form

urlpatterns = [
    path('', blog, name='blog'),
    path('post_form/', post_form, name='post_form'),
]