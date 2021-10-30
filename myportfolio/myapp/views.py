from django.shortcuts import render


# Create your views here.

def home(req):
    return render(req, "home.html")


def exp(req):
    return render(req, "experimental.html")
