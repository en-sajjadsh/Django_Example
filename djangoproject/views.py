from django.shortcuts import HttpResponse,render
import requests , datetime

def indexWebsite(request):
    args = {}
    args["news"] = getLimitNews()
    args["about"] = getAbout()

    return render(request, 'home.html')



def getLimitNews():
    url = "http://api.mediastack.com/v1/news"
    data = {}
    data["access_key"] = "6fbf02afe7f4d6b5bcb82c2a20fab787"
    data["languages"] = "en"
    data["limoit"] = "10"
    data["offset"] = "0"
    data["date"] = datetime.now()
    res = requests.post(url,data=data)

    if res.status_code == 200:
        return res.json()
    else:
        return "Error.not connect to server!!!!"

def getAbout():
    dict = {}


def getNews(page,date):
    url = "http://api.mediastack.com/v1/news"
    data = {}
    data["access_key"] = "6fbf02afe7f4d6b5bcb82c2a20fab787"
    data["languages"] = "en"
    data["limoit"] = "10"
    data["offset"] = page
    data["date"] = date
    res = requests.post(url, data=data)

    if res.status_code == 200:
        return res.json()
    else:
        return "Error.not connect to server!!!!"