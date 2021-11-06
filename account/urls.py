from django.urls import path ,include

from djangoproject import settings
from django.conf.urls.static import static

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns, urlpatterns

app_name = 'account'
urlpatterns = [
    path('signin', views.signin),
    path('signup', views.signup),
    path('forget', views.forget),
    path('status',views.statusPage,name='status')
]