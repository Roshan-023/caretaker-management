from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Blog, Review
from .serializers import BlogSerializer, ReviewSerializer

class BlogCreateAPIView(APIView):
    def post(self, request):
        # Extract the currently authenticated user from the request
        author = request.user  # Assuming the user is authenticated and has been properly set in the request

        # Add the author to the request data before serializing
        request.data['author'] = author.id  # Assuming the author field expects the user's ID

        # Serialize the data and create the blog post
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogListAPIView(APIView):
    def get(self, request):
        # Retrieve all blogs from the database
        blogs = Blog.objects.all()

        # Serialize the queryset
        serializer = BlogSerializer(blogs, many=True)

        # Return the serialized data as a JSON response
        return Response(serializer.data)

class BlogDetailAPIView(APIView):
    def get(self, request, blog_id):
        try:
            # Retrieve the blog object from the database
            blog = Blog.objects.get(pk=blog_id)

            # Serialize the blog object
            serializer = BlogSerializer(blog)

            # Check if the user has already provided a review for this blog
            if request.user.is_authenticated:
                try:
                    review = Review.objects.get(blog=blog, user=request.user)
                    serializer.data['user_rating'] = review.rating
                except Review.DoesNotExist:
                    pass

            # Return the serialized data as a JSON response
            return Response(serializer.data)
        except Blog.DoesNotExist:
            return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)

class ReviewCreateAPIView(APIView):
    def post(self, request, blog_id):
        # Get the blog object corresponding to the provided blog ID
        try:
            blog = Blog.objects.get(pk=blog_id)
        except Blog.DoesNotExist:
            return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Assign the current logged-in user to the review's user field
        user = request.user

        # Create a review serializer with the data from the request
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            # Save the review with the blog and user
            serializer.save(user=user, blog=blog)
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserBlogReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        blog_id = self.kwargs.get('blog_id')
        return Review.objects.filter(user=user, blog_id=blog_id)

class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        blog = self.get_object()

        # Check if the user is the author of the blog
        if blog.author != request.user:
            return Response({"detail": "You do not have permission to delete this blog."}, status=status.HTTP_403_FORBIDDEN)

        blog.delete()
        return Response({"detail": "Blog deleted successfully."}, status=status.HTTP_204_NO_CONTENT)