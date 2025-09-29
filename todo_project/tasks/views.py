from django.shortcuts import render, redirect
from .models import Tasks

def task_list(request):
    tasks = Tasks.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Tasks.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_complete(request, task_id):
    tasks = Tasks.objects.get(id=task_id)
    tasks.completed = True
    tasks.save()
    return redirect('task_list')

def task_delete(request, task_id):
    tasks = Tasks.objects.get(id=task_id)
    tasks.delete()
    return redirect('task_list')