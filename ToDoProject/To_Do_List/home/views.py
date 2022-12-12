from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Task


# Create your views here.

def index(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        if len(task.strip()) == 0:
            return render(request, "home/index.html", {'tasks': Task.objects.all()})
        new_task = Task(task=task)
        new_task.save()
        return render(request, "home/index.html", {'tasks': Task.objects.all()})
    return render(request, "home/index.html", {'tasks': Task.objects.all()})


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('/')
