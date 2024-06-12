from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('hello/entry', views.myform, name='myform'),
    path('hello/panel', views.panel, name='panel'),
    path('hello/nuevoregistro', views.nuevo_registro, name='nuevoregistro'),
]