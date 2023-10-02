from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("generate_teachers/", views.generate_teachers, name="generate_teachers"),
]
