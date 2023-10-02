from django.http import HttpResponse


def index(request):
    return HttpResponse("Index page.")


def generate_teachers(request):
    return HttpResponse("Generate_teachers page.")
