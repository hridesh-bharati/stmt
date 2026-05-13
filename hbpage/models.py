# D:\Hridesh_codes\stmt\hbpage\models.py
from django.db import models
from django.utils import timezone

class Admission(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    
    student_photo = models.ImageField(upload_to='students/photos/', blank=True, null=True)
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    adhar_no = models.CharField(max_length=12, blank=True, null=True)
    address = models.TextField()
    admission_class = models.CharField(max_length=20)
    admission_date = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} ({self.admission_class})"
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    
    student_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    admission_class = models.CharField(max_length=20)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    student_photo = models.ImageField(upload_to='students/photos/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.admission_class}"