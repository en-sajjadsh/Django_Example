import json
from aifc import Error
from builtins import dict
from django.shortcuts import HttpResponse, render,redirect
import http.client, urllib.parse, random
from datetime import datetime
from  django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . import models,forms
from . import Enum
from account import forms as formsAccount


def indexWebsite(request):
    args = getValues(request)

    return render(request, 'home.html', args)


def contact(request):
    if request.method == 'POST':
        form = forms.formContact(request.POST)
        if form.is_valid():
            form.save()
            state = "Success"
            text = "Your context was sended successful for me. ✔"
            args = {}
            args["state"] = state
            args["text"] = text
            request.session['status'] = args
            return redirect('account:state')
    else:
        state = "Error"
        text = "Your context was sended an error. Please try again. ✖"
        type = "signup"
        args = {}
        args["state"] = state
        args["text"] = text
        args["type"] = type
        request.session['status'] = args
        return redirect('account:state')



def hello(request,val):
    print("1234"+val)
    args = getValues(request)

    return render(request, 'home.html', args)

def getValues(request):
    args = {}
    args["title"] = Enum.Type.Home.value
    # change news value
    args["news"] = {'text': 'Error', 'body': "Error"}
    args["about"] = getAbout()
    args["contact"] = getContact()
    args["services"] = getServices()
    args["form_contant"] = forms.formContact()
    args["form_signup"] = formsAccount.formCreateUser()
    args["form_user"] = UserCreationForm()

    return args


def getLimitNews():
    try:
        conn = http.client.HTTPConnection('api.mediastack.com')
        params = urllib.parse.urlencode({
            'access_key': '50aea71714bcc5bf8952ed97759231a6',
            'languages': 'en',
            'offset': '0',
            'date': '2021-09-14',
            'limit': 10,
        })

        conn.request('GET', '/v1/news?{}'.format(params))
        res = conn.getresponse()
        data = res.read()
        jdata = json.loads(str(data.decode('utf-8')))

        list = []
        a = 0000
        for n in jdata["data"]:
            DT = (n["published_at"]).split('T')
            new = news(a, n["author"], n["image"], n["title"], n["description"], n["url"], n["category"],
                       DT[0], DT[1])
            a += 1
            list.append(new)
        return {'text': 'Secces', 'body': list}
    except Error:
        return {'text': 'Error', 'body': Error}


def getAbout():
    dict = {}
    dict["info"] = models.Info.objects.filter(id=1)
    dict["what"] = models.What.objects.filter(person_id=1)
    dict["skill"] = models.Skill.objects.filter(person_id=1)
    dict["education"] = models.Education.objects.filter(person_id=1)
    dict["entertainment"] = models.Entertainment.objects.filter(person_id=1)
    dict["experience"] = models.Experience.objects.filter(person_id=1)
    return dict


def getServices():
    Services = models.Services.objects.all()
    Framework = models.Framework.objects.all()
    Property = models.Property.objects.all()
    Technology = models.Technology.objects.all()
    dict = {
        'service': Services,
        'framework': Framework,
        'property': Property,
        'technology': Technology
    }
    return dict


def getContact():
    dict = {}
    data = models.Info.objects.get(id=1)
    dict["address"] = data.address
    dict["phone"] = data.phone
    dict["email"] = data.email
    dict["website"] = data.website
    return dict


# def getNews(page, date):
#     url = "http://api.mediastack.com/v1/news"
#     data = {}
#     data["access_key"] = "6fbf02afe7f4d6b5bcb82c2a20fab787"
#     data["languages"] = "en"
#     data["limoit"] = "10"
#     data["offset"] = page
#     data["date"] = date
#     res = requests.post(url, data=data)
#
#     if res.status_code == 200:
#         return res.json()
#     else:
#         return "Error.not connect to server!!!!"


class news:
    def __init__(self, id, auther, image, title, discription, url, category, date, time):
        self.id = id
        self.auther = auther
        self.title = title
        self.discription = discription
        self.image = image
        self.url = url
        self.category = category
        self.date = date
        self.time = time
