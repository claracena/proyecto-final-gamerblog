from django.urls import path
from api.views import apiOverview, blogList, blogDetail, commentDetail

urlpatterns = [
    path('', apiOverview, name='api'),
    path('blog-list/', blogList, name='blog-list'),
    path('blog-detail/<int:pk>', blogDetail, name='blog-detail'),
    path('comments/<int:pk>', commentDetail, name='comments'),
]