# forms.py
from django import forms
from .models import Student

class add(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
