from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def home_view(request):
    return HttpResponse("<h1>HOME</h1>")


def about_view(request):
    return HttpResponse("<h1>ABOUT PAGE</h1>")


def contact_view(request):
    return HttpResponse("<h1>contact page</h1>")