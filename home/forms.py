from django import forms
from . import models


class formContact(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = "__all__"
        labels = {
            'user' : 'Name',
            'email' : 'Email',
            'text' : 'Text'
        }
