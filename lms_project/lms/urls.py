from django.urls import path
from .views import CourseListCreateView, LessonListCreateView, StudentListCreateView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
]