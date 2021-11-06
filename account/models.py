from django.db import models

# Create your models here.
class Info_Person(models.Model):
    fname = models.CharField(max_length=20, null=True, blank=True)
    lname = models.CharField(max_length=20, null=True, blank=True)
    specialty = models.CharField(max_length=50, null=True, blank=True)
    born = models.DateField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)


class Password(models.Model):
    person = models.OneToOneField(Info_Person, on_delete=models.CASCADE)
    user = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
