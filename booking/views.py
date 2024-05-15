from django.shortcuts import render
from rest_framework import status
from .serializers import BookingSerializer, NannyGetBookings, PostRatings
from .models import Booking, RateNanny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from myNannyApplication.models import Profile


class BookingCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingListview(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication for GET

    def get(self, request, format=None):
        user = request.user  # Get currently logged-in user
        bookings = Booking.objects.filter(user=user)  # Filter bookings for the user
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

class ProfileBookingListView(APIView):

    permission_classes = [IsAuthenticated]  # Optional: Require authentication

    def get(self, request, id, format=None):
        try:
            profile = Profile.objects.get(pk=id)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

        # Filter bookings for the provided profile
        bookings = Booking.objects.filter(profile=profile)
        serializer = NannyGetBookings(bookings, many=True)
        return Response(serializer.data)

class RatingsCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = PostRatings(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RatingsRetrieveView(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication for GET

    def get(self, request, format=None):
        ratings = RateNanny.objects.all()
        serializer = PostRatings(ratings, many=True)
        return Response(serializer.data)