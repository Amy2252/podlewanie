from django.shortcuts import render,redirect
from django.http import HttpResponse

from power_socket.models import Power_Socket


# Create your views here.

def home(response):
    return render(response,"power_socket/home.html",{})

def outlet(response):
    return HttpResponse("coming soon")

def socket(response,id):
    socket=Power_Socket.objects.get(id=id)
    return render(response,"power_socket/gniazdko.html",{"socket":socket})

def random(response):
    return render(response,"power_socket/home.html",{})

def on(response,id):
    
    socket=Power_Socket.objects.get(id=id)
    socket.turn_on()
    return render(response,"power_socket/gniazdko.html",{"socket":socket})
def off(response,id):
    
    socket=Power_Socket.objects.get(id=id)
    socket.turn_off()
    return render(response,"power_socket/gniazdko.html",{"socket":socket})