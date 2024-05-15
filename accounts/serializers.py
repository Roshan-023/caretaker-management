from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *

from rest_framework import serializers

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
   def validate(self,attr):
    data = super().validate(attr)
    token = self.get_token(self.user)
    data['user'] = str(self.user)
    data['id'] = str(self.user.id)
    data['name'] = str(self.user.name)
    return data
