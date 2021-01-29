from django.urls import path
from upload import views



urlpatterns = [
    path("", views.index, name="index"),
    path("upload", views.upload, name="upload")
]