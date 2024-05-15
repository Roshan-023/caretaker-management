from django.shortcuts import render
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination

class PostListCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all().select_related('author')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data, context={'user' : request.user})
        serializer.is_valid(raise_exception=True)
        # print(request.user)
        serializer.save(author = request.user)
        return Response(serializer.data, status=201)


class PostDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=404)


class CommentListView(ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        # Get all comments for the specified post along with their replies
        return Comment.objects.filter(post_id=post_id).select_related('author').prefetch_related('replies')


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(author=self.request.user, post_id=post_id)


class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        user = request.user

        if not post.likes.filter(id=user.id).exists():
            post.likes.add(user)

        # Remove user from dislikes if already disliked
        if post.dislikes.filter(id=user.id).exists():
            post.dislikes.remove(user)

        return Response(status=status.HTTP_200_OK)

class DislikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        user = request.user

        if not post.dislikes.filter(id=user.id).exists():
            post.dislikes.add(user)

        # Remove user from likes if already liked
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)

        return Response(status=status.HTTP_200_OK)

class LikeCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, comment_id):
        comment = Comment.objects.get(pk=comment_id)
        user = request.user

        if not comment.likes.filter(id=user.id).exists():
            comment.likes.add(user)

        # Remove user from dislikes if already disliked
        if comment.dislikes.filter(id=user.id).exists():
            comment.dislikes.remove(user)

        return Response(status=status.HTTP_200_OK)

class DislikeCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, comment_id):
        comment = Comment.objects.get(pk=comment_id)
        user = request.user

        if not comment.dislikes.filter(id=user.id).exists():
            comment.dislikes.add(user)

        # Remove user from likes if already liked
        if comment.likes.filter(id=user.id).exists():
            comment.likes.remove(user)

        return Response(status=status.HTTP_200_OK)