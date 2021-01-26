from django.db import models
from app.storage_backends import TestS3MediaStorage
import os

# Create your models here.

def upload_to_session_key_dir(instance, filename):
    return os.path.join(instance.session_key, filename)

class TestS3Upload(models.Model):
    session_key = models.CharField(max_length=50, null=False, blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=upload_to_session_key_dir)