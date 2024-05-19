from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from .models import Profile, Domain
from .serializers import VerificationSerializer, DomainSerializer, ProfilePatchSerializer

class VerificationView(APIView):
    def post(self, request, format=None):
        serializer = VerificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerificationListView(APIView):
    def get(self, request, format=None):
        verifications = Profile.objects.all()
        serializer = VerificationSerializer(verifications, many=True)
        return Response(serializer.data)

class VerificationPatchView(APIView):
    def patch(self, request, pk, format=None):
        try:
            verification = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        verification.status = True
        verification.save()

        serializer = VerificationSerializer(verification)
        return Response(serializer.data)

class ProfilePatchView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePatchSerializer

    def get_object(self):
        # Retrieve the Profile object based on the user making the request
        return self.request.user.profile


class ProfileDeleteView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)