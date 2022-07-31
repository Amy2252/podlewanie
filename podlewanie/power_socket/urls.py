from django.urls import path
from . import views


urlpatterns=[
    
    path("",views.home,name="home"),
    path("outlet/",views.outlet,name="outlet"),
    path("Socket_<int:id>/",views.socket,name="socket"),
    path("random/",views.random,name="random"),
    path("Socket_<int:id>/on",views.on,name="on"),
    path("Socket_<int:id>/off",views.off,name="off"),

]