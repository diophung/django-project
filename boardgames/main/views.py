from django.shortcuts import render


def home(request):
    return render(request, "main/home.html", {'message': 'Hello - world'})
