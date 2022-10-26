from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create.as_view()),
    path("", views.List.as_view()),
]