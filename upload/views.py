from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

from .forms import TestS3UploadForm

def test_s3_upload(request):

    # create session if it doesn't already exist
    if not request.session.session_key:
        request.session.create()

    # not quite sure how to use this to set upload destination
    session_key = request.session.session_key

    if request.method == 'POST':

        form = TestS3UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse("upload successful!")
    else:
        form = TestS3UploadForm()

    return render(
        request,
        'upload/test_s3_upload.html',
        {
            'form': form
        }
    )