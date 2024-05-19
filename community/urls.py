from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentListView, CommentCreateAPIView,LikePostView, DislikePostView, LikeCommentView, DislikeCommentView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/comments/', CommentListView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/comments/write/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('posts/<int:post_id>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:post_id>/dislike/', DislikePostView.as_view(), name='dislike-post'),
    path('comments/<int:comment_id>/like/', LikeCommentView.as_view(), name='like-comment'),
    path('comments/<int:comment_id>/dislike/', DislikeCommentView.as_view(), name='dislike-comment'),
]