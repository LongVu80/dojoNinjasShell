from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("createDojo", views.create_dojo),
    path("createNinja", views.create_ninja),
    path("dojo/<int:dojo_id>/delete", views.delete_dojo),
    path("ninja/<int:ninja_id>/delete", views.delete_ninja)
]
