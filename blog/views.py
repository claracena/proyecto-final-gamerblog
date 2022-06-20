from django.shortcuts import render
from blog.models import Blog

# Create your views here.

# def blogview(request):
#     return render(request, 'blog/blog.html')

def blog(request):
    post = Blog.objects.all()
    context = {'post': post}
    return render(request, 'blog/blog.html', context=context)