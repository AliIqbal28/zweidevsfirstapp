from django.db import models


class SoftwareHouse(models.Model):
    name = models.CharField(max_length=255, unique=True)
    about = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    ASSOCIATE_SOFTWARE_ENGINEER = 'ASE'
    LEAD_SOFTWARE_ENGINEER = 'LSE'
    CHIEF_TECHNICAL_OFFICERS = 'CTO'
    DESIGNATION_CHOICES = [
        (ASSOCIATE_SOFTWARE_ENGINEER, 'Associate Software Engineer'),
        (LEAD_SOFTWARE_ENGINEER, 'Lead Software Engineer'),
        (CHIEF_TECHNICAL_OFFICERS, 'Chief Technical Officer'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    software_house = models.ForeignKey(SoftwareHouse, on_delete=models.CASCADE, related_name="employees")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    designation = models.CharField(max_length=3, choices=DESIGNATION_CHOICES, default=ASSOCIATE_SOFTWARE_ENGINEER)
