from django.shortcuts import render, redirect
from shop.models import Tasklist
from shop.forms  import TaskForm
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.

def todolist(request):
    #return HttpResponse('''shop site''')
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("New Task Added!"))
        return redirect('todolist')
    else:

        all_task = Tasklist.objects.all
    # context= {'welcome_text':"welcome todo list page"}
    return render(request, 'todolist.html', {'all_task': all_task})


def delete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')


def contact(request):

    context = {
        'contact_text': " welcome contact page."
    }
    return render(request, 'contact.html', context)


def about(request):
    context = {
        'about_text': "welcome about page."
    }
    return render(request, 'about.html', context)


def edit_task(request, task_id):
    if request.method == "POST":
        task = Tasklist.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, ("Task Edited!"))
            return redirect('todolist')
    else:

        task_obj = Tasklist.objects.get(pk=task_id)
        # context= {'welcome_text':"welcome todo list page"}
    return render(request, 'edit.html', {'task_obj': task_obj})


def complete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect('todolist')


def pending_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')


def index(request):
    return render(request, 'index.html')
