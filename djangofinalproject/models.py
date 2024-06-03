from django.db import models

# Create your models here.

class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True, blank=False) #BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    gender = models.CharField(max_length=55, blank=False) #VARCHAR(55)
    date_created = models.DateTimeField(auto_now_add=True) #TIMSTAMP DEFAULT CURRENT_TIMESTAMP
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'genders'

    
    def __str__(self):
        return self.gender

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True, blank=False)
    first_name = models.CharField(max_length=55, blank=False)
    middle_name = models.CharField(max_length=55, blank=True)
    last_name = models.CharField(max_length=55, blank=False)
    age = models.IntegerField(blank=False) #INT NOT NULL
    birth_date = models.DateField(blank=False) #DATE NOT NULL
    address = models.CharField(max_length=55, blank=False)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    guardian_name = models.CharField(max_length=55, blank=False)
    contact = models.IntegerField(blank=False) #INT NOT NULL
    username = models.CharField(max_length=55, blank=False)
    password = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True) #TIMSTAMP DEFAULT CURRENT_TIMESTAMP
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'