from django import forms
from . import models

class formCreateUser(forms.ModelForm):
    class Meta:
        model = models.Info_Person
        fields = "__all__"
        labels = {
            'fname' : 'First Name',
            'lname' : 'Last Name',
            'specialty' : 'Special',
            'born' : 'Born Date',
            'phone' : 'Phone Number',
            'email' : 'Email Address'
        }
        widgets = {
            # 'born' : forms.DateInput(attrs=["date"]),
            'born' : forms.DateInput(format=('%d-%m-%Y'),
                                             attrs={'type':'date',
                                            'placeholder':'Select a date'}),
            'email' : forms.EmailInput()
        }



class formCreateUserPassword(forms.ModelForm):
    class Meta:
        model = models.Password
        fields = [
            'user',
            'password'
        ]
        labels = {
            'user' : 'Username',
            'password' : 'Password'
        }
        widgets = {
            'password' : forms.PasswordInput()
        }



class formCheckUserPass(forms.ModelForm):
    class Meta:
        model = models.Password
        fields = [
            'user',
            'password'
        ]
        labels = {
            'user': 'Username',
            'password': 'Password'
        }
        widgets = {
            'password': forms.PasswordInput()
        }


class formForgetPassword(forms.ModelForm):
    class Meta:
        model = models.Password
        fields = [
            'user'
        ]
        labels = {
            'user': 'Username'
        }


class formForgetUser(forms.ModelForm):
    class Meta:
        model = models.Info_Person
        fields = [
            'email'
        ]
        labels = {
            'email' : 'Email'
        }