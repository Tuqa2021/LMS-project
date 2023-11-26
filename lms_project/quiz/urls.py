from django.urls import path
from .views import QuizListCreateView, QuizSubmissionCreateView

urlpatterns = [
    path('quizzes/', QuizListCreateView.as_view(), name='quiz-list-create'),
    path('quiz-submissions/', QuizSubmissionCreateView.as_view(), name='quiz-submission-create'),
    
]
