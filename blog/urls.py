from django.urls import path
from blog.views import blog, post_form, article
from django.conf import settings
from django.conf.urls.static import static
from account.views import userProfile

urlpatterns = [
    path('', blog, name='blog'),
    path('post_form/', post_form, name='post_form'),
    path('article/<str:pk>', article, name='article'),
    path('user-profile/<str:pk>', userProfile, name='user-profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)