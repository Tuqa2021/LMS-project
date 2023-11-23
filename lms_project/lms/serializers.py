from rest_framework import serializers
from .models import Course, Lesson, Exam, Student, Certificate

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    # lessons = LessonSerializer(many=True, read_only=True)
    # exams = ExamSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['title','description','cover_image','duration_hours','category','lang']

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['title']

class StudentSerializer(serializers.ModelSerializer):
    enrolled_courses = CourseSerializer(many=True, read_only=True)
    certificates = CertificateSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ['name','enrolled_courses','certificates']
