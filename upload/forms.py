from django import forms
from .models import TestS3Upload

class TestS3UploadForm(forms.ModelForm):

    class Meta:
        model = TestS3Upload
        fields = ['file', 'session_key']
        widgets = {'session_key': forms.HiddenInput()}
