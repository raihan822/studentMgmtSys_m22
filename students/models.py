from django.db import models

# Create your models here.

class Student(models.Model):
    COURSE_CHOICES = [
        ('math', 'Mathematics'),
        ('sci', 'Science'),
        ('eng', 'Engineering'),
        ('art', 'Arts'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)

    def __str__(self):
        return self.name