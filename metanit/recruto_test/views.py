from django.shortcuts import render


def index(request):
    message = request.GET.get("message")
    name = request.GET.get("name")
    data = {'message': message, 'name': name}
    return render(request, "index1.html", context=data)


