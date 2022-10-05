from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('male', "Male"),
        ('female', "Female"),
    )
    #user = models.ForeignKey(User, on_delete= models.CASCADE )
    profile_owner = models.OneToOneField(User, on_delete= models.CASCADE, related_name='user_creator')
    created_on = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=7, choices= GENDER_CHOICES)

    class Meta:
        ordering = ['created_on']
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
    
    def __str__(self):
        return self.profile_owner.username
    
    def full_name(self):
        return self.first_name + ' ' + self.last_name