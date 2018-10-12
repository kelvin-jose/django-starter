from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
     url('index/',views.index,name='index'),
     url('show/',views.show,name='show'),
     url('save/',views.save,name='save'),
]