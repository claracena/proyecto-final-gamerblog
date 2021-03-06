from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import Q
from .models import Blog, Comment
from .forms import ArticleForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class HomeView(ListView):
    paginate_by = 3
    model = Blog
    template = 'blog/blog_list.html'
    ordering = ['-id']

class ArticleDetailView(FormMixin, DetailView):
    model = Blog
    template = 'blog/blog_detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('article', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.blog_comment.blog_id = self.object.id
        form.instance.author = self.request.user
        form.save()
        return super(ArticleDetailView, self).form_valid(form)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template = 'blog/blog_form.html'
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def detailViewComment(request, pk):
    articulo = Blog.objects.get(id=pk)
    comments = Comment.objects.filter(blog=pk).select_related('author').order_by('-id')
    count = comments.count()
    form = CommentForm
    context = {'blog': articulo, 'form': form, 'comments': comments, 'count': count}

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.blog_id = pk
            form.instance.author_id = request.user.id
            form.save()
            # return render(request, 'blog/blog_detail.html', context=context)
            return redirect('article', pk=pk)

    return render(request, 'blog/blog_detail.html', context=context)

def searchView(request):
    if request.GET.get('search') is not None:
        search_text = request.GET.get('search')
        results = Blog.objects.filter(Q(title__icontains=search_text) | Q(body__icontains=search_text))
        page = request.GET.get('page', 1)
        paginator = Paginator(results, 5)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return render(request, 'blog/blog_search.html', {'results': posts, 'search': search_text})

    return render(request, 'blog/blog_search.html')
