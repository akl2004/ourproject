from django.db import models

class Student(models.Model):
    GENDER_CHOICES = (
        ('N/A', 'N/A'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    student_id = models.BigAutoField(primary_key=True, blank=False)  # BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    first_name = models.CharField(max_length=55, blank=False)
    middle_name = models.CharField(max_length=55, blank=True)
    last_name = models.CharField(max_length=55, blank=False)
    age = models.IntegerField(blank=False)  # INT NOT NULL
    birth_date = models.DateField(blank=False)  # DATE NOT NULL
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255, blank=False)
    contact = models.CharField(max_length=13, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'students'

class Academic(models.Model):
    CLASSIFICATION_CHOICES = (
        ('N/A', 'N/A'),
        ('DROPPED', 'DROPPED'),
        ('REGULAR', 'REGULAR'),
        ('IRREGULAR', 'IRREGULAR'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='academics')
    id_number = models.CharField(max_length=12, blank=False)
    course = models.CharField(max_length=55, blank=False)
    year_level = models.IntegerField(blank=False)  # INT NOT NULL
    section = models.CharField(max_length=55, blank=False)
    semester = models.CharField(max_length=55, blank=False)
    ay = models.CharField(max_length=9, blank=False)  # Adjusted to '9' to accommodate '2023-2024' format
    classification = models.CharField(max_length=10, choices=CLASSIFICATION_CHOICES)

    class Meta:
        db_table = 'academic'

        
