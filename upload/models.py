from django.db import models
from app.storage_backends import TestS3MediaStorage

# Create your models here.

class TestS3Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=TestS3MediaStorage())