from django.shortcuts import render
from django.http import HttpResponse
from .forms import TestS3UploadForm
from .models import TestS3Upload

# Create your views here.

def upload(request):

    # create session if it doesn't already exist
    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key

    if request.method == 'POST':

        form = TestS3UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            filename = "{}/{}".format(session_key, form.cleaned_data['file'].name)
            s3_upload_path = TestS3Upload.objects.get(file=filename).file.url

            return HttpResponse("Image successfully uploaded to bucket at location: {}".format(s3_upload_path))
    else:
        form = TestS3UploadForm(initial={'session_key': session_key})

    return render(
        request,
        'upload/upload.html',
        {
            'form': form
        }
    )

def index(request):
    return render(
        request,
        'upload/index.html',
        {}
        )