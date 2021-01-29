from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TestS3UploadForm
from .models import TestS3Upload

from django.contrib import messages

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

            return redirect(index)
            # return HttpResponse("Image successfully uploaded to bucket at location: {}".format(s3_upload_path))
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
    images = TestS3Upload.objects.all()
    print(len(images))
    return render(
        request,
        'upload/index.html',
        {
            'images': images
        }
        )

def delete(request, file):
    try:
        file = TestS3Upload.objects.get(file=file)
        file.delete()
        messages.success(request, 'File successfully deleted.')
    except TestS3Upload.DoesNotExist:
        pass
    return redirect(index)