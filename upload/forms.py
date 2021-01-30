from django import forms
from .models import Upload

class UploadForm(forms.ModelForm):

    class Meta:
        model = Upload
        fields = [
            'file', 
            'session_key'
            ]
        widgets = {
            'session_key': forms.HiddenInput()
            }
        labels = {
            'file': 'Select an Image to upload',
        }