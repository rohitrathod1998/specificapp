from django.shortcuts import render

# Create your views here.
def send(request):
    return render(request,'send.html')