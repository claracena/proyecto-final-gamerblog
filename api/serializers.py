from rest_framework import serializers
from blog.models import Blog, Comment

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ('id', 'title', 'pub_date', 'body', 'image')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('blog', 'comment_date', 'message', 'author')
