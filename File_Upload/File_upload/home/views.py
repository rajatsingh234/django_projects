from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .models import File
from django.contrib import messages


def upload_file(request):
    if request.method == 'POST':
        file= request.FILES["file"]
        document= File.objects.create(my_file=file)
        document.save()
        messages.success(request,"File uploaded successfully!")
        return render(request, 'home/index.html')

    return render(request, 'home/index.html')
