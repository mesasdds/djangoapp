from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages

def taskList(request):

    search = request.GET.get('search')

    if search:
        
        tasks = Task.objects.filter(title__icontains=search)

    else:

        tasks_list = Task.objects.all().order_by('-created_at')
        paginator = Paginator(tasks_list, 3)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task':task})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form':form})
    

def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form':form, 'task':task})
    else:
        return render(request, 'tasks/edittask.html', {'form':form, 'task':task})



def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    
    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('/')

def helloWorld(request):
    return HttpResponse('Hello World')

def yourName(request, name):
    return render(request, 'tasks/yourname.html', { 'name': name })