from django.urls import path
from django.http import HttpResponse
from AppCoder.views import *

urlpatterns = [
    path("cursos/", cursos_view),
    path("inicio", inicio_view)
]