# hbpage/models.py
from django.db import models
from django.utils import timezone

class Admission(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    
    student_photo = models.ImageField(upload_to='students/photos/', blank=True, null=True)
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    adhar_no = models.CharField(max_length=12, blank=True, null=True) # Aadhaar field
    address = models.TextField()
    admission_class = models.CharField(max_length=20)
    admission_date = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} ({self.admission_class})"

class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class StudentRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name