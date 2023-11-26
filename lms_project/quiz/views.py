from django.shortcuts import render
from rest_framework import generics
from .models import Lesson, Quiz, QuizSubmission
from .serializers import LessonSerializer, QuizSerializer, QuizSubmissionSerializer

class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizSubmissionCreateView(generics.CreateAPIView):
    queryset = QuizSubmission.objects.all()
    serializer_class = QuizSubmissionSerializer

    def perform_create(self, serializer):
        # Ensure that a user can submit the quiz only once
        user = self.request.user
        quiz_id = self.request.data.get('quiz')
        if QuizSubmission.objects.filter(user=user, quiz_id=quiz_id).exists():
            raise serializers.ValidationError("Quiz already submitted.")
        serializer.save(user=user)
