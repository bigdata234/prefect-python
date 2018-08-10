from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def t1(request):
    return HttpResponse("<html>The First Test!</html>")
