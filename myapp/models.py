from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models
# Create your models here.


class Student(models.Model):
    sid = models.CharField(max_length = 16)
    name = models.CharField(max_length = 60)
    age = models.IntegerField()
    gender = models.CharField(max_length = 10)
    cgpa = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(4.0)])
    graduated = models.BooleanField()
    
    def __str__(self):
        return self.name
    