from django.urls import path
from .views import CustomUserListCreateView

urlpatterns = [
    path('users/', CustomUserListCreateView.as_view(), name='customuser-list-create'),
]
