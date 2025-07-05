from django.urls import path
from .views import UserCreateView, CustomTokenObtainPairView, UserListView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/', UserListView.as_view(), name='user-list'),
]