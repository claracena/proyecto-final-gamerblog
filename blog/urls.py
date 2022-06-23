from django.urls import path
# from blog.views import blog, post_form, article
from blog.views import HomeView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, detailViewComment, searchView
from django.conf import settings
from django.conf.urls.static import static
from account.views import userProfile

urlpatterns = [
    path('', HomeView.as_view(), name='blog'),
    path('article/<int:pk>', detailViewComment, name='article'),
    path('new-article/', ArticleCreateView.as_view(), name='article-post'),
    path('update-article/<int:pk>', ArticleUpdateView.as_view(), name='article-update'),
    path('search/', searchView, name='search'),
    # path('post_form/', post_form, name='post_form'),
    # path('article/<str:pk>', article, name='article'),
    # path('user-profile/<str:pk>', userProfile, name='user-profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)