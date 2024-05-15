from rest_framework import serializers
from .models import Blog, Review
from django.conf import settings
from rest_framework.request import Request

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['rating']

class BlogSerializer(serializers.ModelSerializer):
     reviews = ReviewSerializer(many=True, read_only=True)
     class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'content', 'image', 'created_at', 'reviews']

