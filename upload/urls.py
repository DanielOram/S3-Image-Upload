from django.urls import path
from upload import views



urlpatterns = [
    path("", views.test_s3_upload)
]