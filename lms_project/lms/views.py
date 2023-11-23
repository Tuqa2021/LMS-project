from rest_framework import generics
from .models import Course, Lesson, Student
from .serializers import CourseSerializer, LessonSerializer, StudentSerializer
from rest_framework import routers, serializers, viewsets

class CourseListCreateView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonListCreateView(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class StudentListCreateView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

