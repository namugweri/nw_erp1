from django.db import models

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    contact=models.CharField(max_length=200)
    nin=models.CharField(max_length=50)
    photo = models.ImageField(upload_to ='uploads/')
    GENDER_CHOICES = [
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    
    ]
    GENDER = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    DOB = models.DateField()
    
