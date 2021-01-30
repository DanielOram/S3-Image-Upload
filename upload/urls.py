from django.urls import path
from upload import views



urlpatterns = [
    path("", views.index),
    path("<str:view>", views.index, name="index"),
    path("upload", views.upload, name="upload"),
    path("delete/<path:file>", views.delete, name="delete")
]