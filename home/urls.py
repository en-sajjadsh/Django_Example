from django.urls import path ,include

from djangoproject import settings
from django.conf.urls.static import static

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns, urlpatterns

app_name = 'home_page'
urlpatterns = [
    path('', views.indexWebsite,name='home'),
    path('contact', views.contact,name='contact'),
]