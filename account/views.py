from django.shortcuts import HttpResponse, render,redirect
from . import forms



def signup(request):
    if request.method == 'POST':
        formUser = forms.formCreateUser(request.POST)
        formPass = forms.formCreateUserPassword(request.POST)
        if formUser.is_valid() and formPass.is_valid():
            form_u = formUser.save()
            form_p = formPass.save(commit=False)
            form_p.person = form_u
            form_p.save()
            state = "Success"
            text = "Your account was created successfully. ✔"
            return redirect('account:status',state,text,None)
    else:
        state = "Error"
        text = "Your account has encountered an error. Please try again. ✖"
        type = "signup"
        return redirect('account:status',state,text,type)


def statusPage(request,state,textState,typeTry):
    args = {}
    args["state"] = state
    args["text"] = textState
    args["type"] = typeTry
    return (request,'state.html',args)


def signin(request):
    return None


def forget(request):
    return None