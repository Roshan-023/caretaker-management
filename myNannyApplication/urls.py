from django.urls import path
from .views import VerificationView, VerificationListView, VerificationPatchView, ProfilePatchView, ProfileDeleteView

urlpatterns = [
    path('', VerificationView.as_view()),
    path('list/', VerificationListView.as_view()),
    path('verifications/<int:pk>/', VerificationPatchView.as_view(), name='verification-patch'),
    path('application/patch/', ProfilePatchView.as_view()),
    path('application/<int:pk>/delete/', ProfileDeleteView.as_view()),
]

