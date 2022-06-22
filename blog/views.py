from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Blog
from .forms import ArticleForm

class HomeView(ListView):
    model = Blog
    template = 'blog/blog_list.html'
    ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Blog
    template = 'blog/blog_detail.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template = 'blog/blog_form.html'
    # fields = ('image', 'title', 'body', 'tags', 'platforms')
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(ArticleCreateView, self).dispatch(*args, **kwargs)

    # def get_queryset(self):
    #     return Blog.objects.filter(author=self.request.user)

# lista de posts
# def blog(request):
#     post = Blog.objects.all()
#     context = {'post': post}
#     return render(request, 'blog/blog.html', context=context)

# # formulario para crear posts
# @login_required(login_url='login')
# def post_form(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             formx = form.save(commit=False)
#             formx.save()
#             return redirect('blog')
#         else:
#             return render(request, 'blog/post_form.html')
#     return render(request, 'blog/post_form.html')

# def article(request,pk):
    # post = Blog.objects.get(id=pk)
    # context = {'post': post}
    # return render(request, 'blog/article.html', context=context)
