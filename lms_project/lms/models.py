from django.db import models

class BaseModel(models.Model):
    creat_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='course_covers/', null=True, blank=True)
    duration_hours = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=100) #choices
    lang = models.CharField(max_length=50) #choices

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)

class Exam(models.Model):
    title = models.CharField(max_length=255)
    questions = models.TextField()
    course = models.ForeignKey(Course, related_name='exams', on_delete=models.CASCADE)

class Certificate(models.Model):
    title = models.CharField(max_length=255)

class Student(models.Model):
    name = models.CharField(max_length=255)
    enrolled_courses = models.ManyToManyField(Course, related_name='enrolled_students')
    certificates = models.ManyToManyField(Certificate, related_name='awarded_students')

    
