from django.urls import path
from .views import BookingListview, BookingCreateView, ProfileBookingListView, RatingsCreateView, RatingsRetrieveView

urlpatterns = [
    path('addBooking/', BookingCreateView.as_view()),
    path('list/', BookingListview.as_view()),
    path('list/<int:id>', ProfileBookingListView.as_view()),
    path('addRating/', RatingsCreateView.as_view()),
    path('getRatings/', RatingsRetrieveView.as_view())
]
