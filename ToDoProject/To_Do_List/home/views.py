from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Task
from django.views.generic import TemplateView, CreateView, DeleteView, ListView
from django.urls import reverse_lazy


# Create your views here.
#
# def index(request):
#     if request.method == 'POST':
#         task = request.POST.get('task')
#         if len(task.strip()) == 0:
#             return render(request, "home/index.html", {'tasks': Task.objects.all()})
#         new_task = Task(task=task)
#         new_task.save()
#         return render(request, "home/index.html", {'tasks': Task.objects.all()})
#     return render(request, "home/index.html", {'tasks': Task.objects.all()})
#
#
# def delete_task(request, task_id):
#     task = Task.objects.get(pk=task_id)
#     task.delete()
#     return redirect('/')

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
class CreateTask(CreateView):
    model = Task
    fields = ('task',)
    # template_name = 'home/base.html'
    success_url = '/'
    # context_object_name = 'tasks'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tasks'] = Task.objects.all()
    #     return context

class DeleteTask(DeleteView):
    model = Task
    success_url = '/'
