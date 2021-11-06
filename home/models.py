from django.db import models
import hashlib


class Info(models.Model):
    fname = models.CharField(max_length=20, null=False, blank=False)
    lname = models.CharField(max_length=20, null=False, blank=False)
    specialty = models.CharField(max_length=50, null=False, blank=False)
    about = models.TextField(max_length=1000, null=False, blank=False)
    born = models.CharField(max_length=10, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    website = models.CharField(max_length=50, null=True, blank=True)


class Password(models.Model):
    person = models.OneToOneField(Info, on_delete=models.CASCADE)
    user = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)


class What(models.Model):
    person = models.ForeignKey(Info, on_delete=models.CASCADE)
    special = models.CharField(max_length=20, null=False, blank=False)
    about = models.CharField(max_length=30, null=False, blank=False)


class Skill(models.Model):
    person = models.ForeignKey(Info, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, null=False, blank=False)
    name = models.CharField(max_length=40, null=False, blank=False)
    value = models.CharField(max_length=5, null=True, blank=True)


class Education(models.Model):
    person = models.ForeignKey(Info, on_delete=models.CASCADE)
    university = models.CharField(max_length=100, null=False, blank=False)
    major = models.CharField(max_length=200, null=False, blank=False)
    dateStart = models.CharField(max_length=10, null=False, blank=False)
    dateEnd = models.CharField(max_length=10, null=False, blank=False)


class Entertainment(models.Model):
    person = models.ForeignKey(Info, on_delete=models.CASCADE)
    value = models.CharField(max_length=20, null=False, blank=False)
    pic = models.CharField(max_length=50, null=False, blank=False)


class Experience(models.Model):
    person = models.ForeignKey(Info, on_delete=models.CASCADE)
    dateStart = models.CharField(max_length=10, null=False, blank=False)
    dateEnd = models.CharField(max_length=10, null=False, blank=False)
    experience = models.CharField(max_length=40, null=False, blank=False)
    title = models.CharField(max_length=40, null=False, blank=False)
    text = models.CharField(max_length=200, null=False, blank=False)


class Services(models.Model):
    type = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=20, null=False, blank=False)
    discription = models.TextField(null=False, blank=False)
    pic = models.ImageField(blank=True, null=True, upload_to='upload_image/')


class Framework(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    discription = models.TextField(max_length=10000, null=False, blank=False)


class Property(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, null=False, blank=False)


class Technology(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    discription = models.TextField(max_length=10000, null=False, blank=False)


class Contact(models.Model):
    user = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100,null=False,blank=False)
    text = models.TextField(max_length=10000, null=False, blank=False)
