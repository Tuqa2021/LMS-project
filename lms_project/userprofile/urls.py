from django.urls import path
from .views import UserProfileListCreateView

urlpatterns = [
    path('profiles/', UserProfileListCreateView.as_view(), name='userprofile-list-create'),
    
]
