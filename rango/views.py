from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("rango says hey there partner!<br/><a href='/rango/about/'>About</a>")
def about(request):
    return HttpResponse("Rango says here is about page. <a href='/rango/'>Index</a>")
