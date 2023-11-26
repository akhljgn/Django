from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="base"),
    path("/view", views.view, name="view"),
    path("/add", views.add, name="add"),
    path("edit/<int:p>", views.edit, name="edit"),
    path("delete/<int:p>", views.delete, name="delete"),
]