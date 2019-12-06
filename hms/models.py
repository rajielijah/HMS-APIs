from django.db import models
from django.contrib.auth.models import User

class Hostel(models.Model):
    name = models.CharField(max_length=100, blank=True)
    gender_choices = [
        ('N', 'None'), ('M', 'Male'), ('F', 'Female')
    ]
    gender = models.CharField(choices = gender_choices, max_length=1)
    no_of_block = models.IntegerField()
    warden = models.OneToOneField('Warden', on_delete=models.CASCADE,default=None, blank=True)
    def __str__(self):
        return self.name

class Block(models.Model):
    name = models.CharField(max_length=1)
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE, blank =True)
    

    def __str__(self):
        return self.name

class Room(models.Model):
    Condition = [
        ('G', 'Good'), ('B', 'Bad'), ('T', 'Terrible')
    ]

    no = models.CharField(max_length=3)
    block = models.ForeignKey('Block', on_delete=models.CASCADE, blank=True)
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE, blank =True)
    condition = models.CharField(choices=Condition, max_length=1)
    def __str__(self):
        return self.no

class Warden(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, blank=True)
    name = models.CharField(max_length=100, help_text = 'Your Full name')
    staff_id = models.CharField(max_length=50)
    
    gender_choices = [
        ('N', 'None'), ('M', 'Male'), ('F', 'Female')
    ]
    gender = models.CharField(choices = gender_choices, max_length=1)

    def __str__(self):
        return self.name