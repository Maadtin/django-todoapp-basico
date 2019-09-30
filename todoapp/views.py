from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def lista_tareas(request):
    tareas = Task.objects.all().order_by('-id')
    return render(request, 'lista.html', {'tareas': list(tareas)})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TaskForm()
    return render(request, 'create-task.html', {'form': form})


def edit_task(request, tarea_id):
    instance = Task.objects.get(pk=tarea_id)
    if request.method == 'POST':
        if 'delete_task' in request.POST:
            instance.delete()
            return redirect('lista_tareas')
        else:
            form = TaskForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('lista_tareas')
    else:
        form = TaskForm(instance=instance)
    return render(request, 'edit-task.html', {'form': form})
