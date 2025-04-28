from django import forms
from django.contrib.auth.models import User
from .models import Student

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['courses']
