from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TestS3UploadForm
from .models import TestS3Upload

from django.contrib import messages



# Create your views here.

def upload(request):

    check_session(request)

    session_key = request.session.session_key

    if request.method == 'POST':

        form = TestS3UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            filename = "{}/{}".format(session_key, form.cleaned_data['file'].name)
            s3_upload_path = TestS3Upload.objects.get(file=filename).file.url
            messages.success(request, "Successfully uploaded file!")
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

def index(request, view="list-view"):

    check_session(request)

    session_key = request.session.session_key

    if request.method == 'POST':

        form = TestS3UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            filename = "{}/{}".format(session_key, form.cleaned_data['file'].name)
            s3_upload_path = TestS3Upload.objects.get(file=filename).file.url
            messages.success(request, "Successfully uploaded file!")
            return redirect(index, view=view)
            # return HttpResponse("Image successfully uploaded to bucket at location: {}".format(s3_upload_path))
    else:
        form = TestS3UploadForm(initial={'session_key': session_key})

    images = TestS3Upload.objects.all()


    if view =='card-view':
        template = 'upload/card_view_index.html'
    else:
        template = 'upload/list_view_index.html'

    return render(
        request,
        template,
        {
            'images': images,
            'form': form
        }
        )
    

def delete(request, file):
    try:
        file = TestS3Upload.objects.get(file=file)
        # file.delete_thumbnails()
        file.delete()
        messages.success(request, 'File successfully deleted.')
    except TestS3Upload.DoesNotExist:
        pass
    return redirect(index)


def check_session(request):
    # create session if it doesn't already exist
    if not request.session.session_key:
        request.session.create()