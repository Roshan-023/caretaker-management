from django.urls import path
from .views import BlogCreateAPIView, BlogListAPIView, ReviewCreateAPIView, BlogDetailAPIView, UserBlogReviewListView, BlogDeleteView

urlpatterns = [
    path('write/', BlogCreateAPIView.as_view(), name='blog-create'),
    path('list/', BlogListAPIView.as_view(), name='blog-list'),
    path('<int:blog_id>/', BlogDetailAPIView.as_view(), name='blog-detail'),
    path('<int:blog_id>/reviews/write/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('<int:blog_id>/reviews/get/', UserBlogReviewListView.as_view(), name='user-blog-reviews'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
]