from django.shortcuts import render, redirect
from .models import Blog
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# lista de posts
def blog(request):
    post = Blog.objects.all()
    context = {'post': post}
    return render(request, 'blog/blog.html', context=context)

# formulario para crear posts
@login_required(login_url='login')
def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            formx = form.save(commit=False)
            formx.save()
            return redirect('blog')
        else:
            messages.error(request, 'Bumbula')
            return render(request, 'blog/post_form.html')
    return render(request, 'blog/post_form.html')

# @login_required(login_url='login')
# def post_form(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.error(request, 'Bumbula')
#             return render(request, 'blog/blog.html') 
#         else:
#             return render(request, 'blog/post_form.html')
#     return render(request, 'blog/post_form.html')
