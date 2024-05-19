from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='User.name')
    replies = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()

    def get_replies(self, obj):
        replies = obj.replies.all()
        return CommentSerializer(replies, many=True).data

    def get_likes_count(self, obj):
        return obj.total_likes()

    def get_dislikes_count(self, obj):
        return obj.total_dislikes()

    class Meta:
        model = Comment
        fields = ('id', 'author', 'content', 'parent', 'created_at',
                   'replies', 'likes_count', 'dislikes_count')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name', read_only=True)
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)


    def get_likes_count(self, obj):
        return obj.total_likes()

    def get_dislikes_count(self, obj):
        return obj.total_dislikes()


    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'desc', 'published_date',
                   'likes_count', 'dislikes_count', 'comments')


