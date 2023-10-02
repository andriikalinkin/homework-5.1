from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Homework-5 index page.</h1>")


def generate_teachers(request):
    return HttpResponse("<h1>Generate_teachers page.</h1>")
