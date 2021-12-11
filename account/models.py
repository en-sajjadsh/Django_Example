from django.contrib.auth.models import User
from django.db import models



class Person(models.Model):
    fname = models.CharField(max_length=20, null=True, blank=True)
    lname = models.CharField(max_length=20, null=True, blank=True)
    specialty = models.CharField(max_length=50, null=True, blank=True)
    born = models.DateField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    User = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.User.username