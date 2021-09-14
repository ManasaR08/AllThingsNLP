from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from .models import FilesUpload

@csrf_exempt
def file_upload(request):
    context = {}
    request_context = RequestContext(request)
    if request.method == 'POST' and request.FILES['myFile']:
        myFile = request.FILES['myFile']
        document = FilesUpload.objects.creat(file=myFile)
        document.save()
        return HttpResponse("File has been uploaded", context, request_context=request_context)
    return render(request, 'index,html')

def home(request):
    if request.method == 'POST':
        clientside_form = FilesUpload(request.POST, request.FILES, instance=request.user)
        if clientside_form.is_valid():
            name = clientside_form.myFile['file_name']
            files = clientside_form.myFile['myFile']
            FilesUpload(file_name=name, files=files)
            return HttpResponse("File Uploaded")
        else:
            return HttpResponse("Error Uploading")
    else:
        return render(request, 'index.html')