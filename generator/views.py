from django.shortcuts import render
# from django.http import HttpResponse
import random


def about(request):
    return render(request, "generator/about.html")

def home(request):
    return render(request, "generator/home.html")

def password(request):

    length = int(request.GET.get("length"))

    if length < 7 or length > 12:
        return render(request, "generator/invalidparams.html")

    characters = list("abcdefghijklmnopqrstuvwxyz")
    generated_password = ""

    if request.GET.get("uppercase") == "on":
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("uppercase") and request.GET.get("uppercase") != "on":
        return render(request, "generator/invalidparams.html")

    if request.GET.get("special") == "on":
        characters.extend(list("~!@#$%^&*()_-=+\|;:'<.>/?"))
    if request.GET.get("special") and request.GET.get("special") != "on":
        return render(request, "generator/invalidparams.html")

    if request.GET.get("numbers") == "on":
        characters.extend(list("0123456789"))
    if request.GET.get("numbers") and request.GET.get("numbers") != "on":
        return render(request, "generator/invalidparams.html")

    for i in range(length):
        generated_password += random.choice(characters)

    return render(request, "generator/password.html", {"password": generated_password})
