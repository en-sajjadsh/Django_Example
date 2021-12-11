from django import forms
from . import models

class formCreateUser(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = 'fname','lname','specialty','born','phone','email'
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

