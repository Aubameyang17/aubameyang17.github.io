from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def user(request):
    age = request.GET.get("age")
    name = request.GET.get("name")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")