from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    age = request.GET.get("age")
    print(age)
    name = request.GET.get("name")
    print(name)
    data = {'age': age, 'name': name}
    return render(request, "index1.html", context=data)


