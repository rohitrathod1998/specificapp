from app2.views import *
from django.urls import path
app_name='outof'
urlpatterns=[
    path('send',send,name='send'),
]