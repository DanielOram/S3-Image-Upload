from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm
from .models import Upload

from django.contrib import messages



# Create your views here.

def upload(request):

    check_session(request)

    session_key = request.session.session_key

    if request.method == 'POST':

        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            filename = "{}/{}".format(session_key, form.cleaned_data['file'].name)
            s3_upload_path = Upload.objects.get(file=filename).file.url
            messages.success(request, "Successfully uploaded file!")
            return redirect(index)
            # return HttpResponse("Image successfully uploaded to bucket at location: {}".format(s3_upload_path))
    else:
        form = UploadForm(initial={'session_key': session_key})

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

        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            filename = "{}/{}".format(session_key, form.cleaned_data['file'].name)
            s3_upload_path = Upload.objects.get(file=filename).file.url
            messages.success(request, "Successfully uploaded file!")
            return redirect(index, view=view)
    else:
        form = UploadForm(initial={'session_key': session_key})

    images = Upload.objects.all()

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
        file = Upload.objects.get(file=file)
        # file.delete_thumbnails()
        file.delete()
        messages.success(request, 'File successfully deleted.')
    except Upload.DoesNotExist:
        pass
    return redirect(index)


def check_session(request):
    # create session if it doesn't already exist
    if not request.session.session_key:
        request.session.create()
        # set session to expire in 24 hrs
        request.session.set_expiry(86400)