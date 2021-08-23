from django.shortcuts import HttpResponse,render

def indexWebsite(request):
    return render(request, 'index.html')