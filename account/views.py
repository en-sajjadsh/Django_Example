from django.shortcuts import render,redirect
from . import forms
from  django.contrib.auth.forms import UserCreationForm,AuthenticationForm




def signup(request):
    if request.method == 'POST':
        formPerson = forms.formCreateUser(request.POST)
        formUser = UserCreationForm(request.POST)
        if formPerson.is_valid() and formUser.is_valid():
            form_u = formUser.save(commit=False)
            form_p = formPerson.save(commit=False)
            form_p.User = form_u
            form_u.save()
            form_p.save()
            args={}
            args["type"] = "success"
            args["text"] = "Your account was created successfully. ✔"
            return redirect('in',args=args)
        else:
            args = {}
            args["type"] = "Error"
            args["text"] = "Your account has exist."
            return redirect('home_page:home', args=args)



# def index(requset):
