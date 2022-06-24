from django.urls import path
from api.views import apiOverview, blogList, blogDetail, commentDetail, tagList, platformList

urlpatterns = [
    path('', apiOverview, name='api'),
    path('blog-list/', blogList, name='blog-list'),
    path('blog-detail/<int:pk>', blogDetail, name='blog-detail'),
    path('comments/<int:pk>', commentDetail, name='comments'),
    path('tag-list/', tagList, name='tag-list'),
    path('platform-list/', platformList, name='platform-list'),
]