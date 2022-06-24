from rest_framework import serializers
from blog.models import Blog, Comment, Tag, Platform

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ('id', 'title', 'pub_date', 'body', 'image', 'tags', 'platforms')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('blog', 'comment_date', 'message')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'
