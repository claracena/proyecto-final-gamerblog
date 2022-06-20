from django.shortcuts import render
from .models import Blog
from .forms import PostForm

# Create your views here.

def blog(request):
    post = Blog.objects.all()
    context = {'post': post}
    return render(request, 'blog/blog.html', context=context)

def post_form(request):
    data = {
        'form' : PostForm(),
    }

    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/post_form.html') 
        else:
            data['form'] = form
    return render(request, 'blog/post_form.html', context=data)


