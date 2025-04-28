from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.user.username

class Report(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student.user.username} - {self.subject}"
