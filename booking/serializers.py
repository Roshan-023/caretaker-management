from rest_framework import serializers
from .models import Booking, RateNanny
from django.contrib.auth import get_user_model

user = get_user_model()

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class NannyGetBookings(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['user', 'domain_name', 'day', 'from_time', 'to_time', 'is_one_time', 'is_recurring', 'price', 'address', 'district', 'postal_code', 'country', 'other_instructions']


class PostRatings(serializers.ModelSerializer):
    class Meta:
        model = RateNanny
        fields = '__all__'