from django.urls import path
from .views import SignUpView, LoginView, ProfileUpdateView, UserListView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('list/', UserListView.as_view())
]
