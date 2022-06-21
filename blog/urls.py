from django.urls import path
from blog.views import blog, post_form
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', blog, name='blog'),
    path('post_form/', post_form, name='post_form'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)