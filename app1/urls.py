from app1.views import *
from django.urls import path
app_name='Into'
urlpatterns=[
    path ('get/',get,name='get'),
]