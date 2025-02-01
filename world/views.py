from django.shortcuts import render
from typing import Any
from django.urls import path


def hello_world(request: Any):
    return render(request, "index.html")


urlpatterns = [
    path('', hello_world, name='world')
]
