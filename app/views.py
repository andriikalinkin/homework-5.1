from django.shortcuts import render

from app.models import Teacher


def index(request):
    return render(request, "index.html")


def generate_teachers(request):
    teachers = Teacher.objects.all()

    return render(request, "generate_teachers.html", {"teachers": teachers})
