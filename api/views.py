from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Blog, Comment
from api.serializers import BlogSerializer, CommentSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/blog-list/',
        'Detail View': '/blog-detail/<int:pk>/',
        'Comments': '/comments/<int:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def blogList(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def blogDetail(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def commentDetail(request, pk):
    comment = Comment.objects.filter(blog_id=pk)
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)
