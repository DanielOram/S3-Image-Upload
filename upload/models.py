from django.db import models
from app.storage_backends import TestS3MediaStorage
import os

from django.dispatch import receiver

from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer

# Create your models here.


def upload_to_session_key_dir(instance, filename):
    return os.path.join(instance.session_key, filename)

class TestS3Upload(models.Model):
    session_key = models.CharField(max_length=50, null=False, blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = ThumbnailerImageField(upload_to=upload_to_session_key_dir, blank=True)

    def filename(self):
        return os.path.basename(self.file.name)


# delete TestS3Upload file from local media 
def _delete_file(path):
   """ Deletes file from filesystem. """
   if os.path.isfile(path):
       print('deleting {} from filesystem'.format(path))
       os.remove(path)

def _delete_thumbnails(file):
    """ Deletes thumbnails of files """
    thumbnailer = get_thumbnailer(file)
    thumbnailer.delete_thumbnails()

@receiver(models.signals.post_delete, sender=TestS3Upload)
def delete_file(sender, instance, *args, **kwargs):
    """ Deletes file on `post_delete` """
    if instance.file:
        _delete_thumbnails(instance.file)
        _delete_file(instance.file.path)