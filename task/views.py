from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, TaskDetail
from datetime import datetime
from .forms import TaskForm
from django.db.models import Q


def index(request):
    if not request.session.get('id', None):
        return redirect("/login/")
    tasks = Task.objects.filter(emp_id=request.session['id']).order_by('-id')
    return render(request, 'task/index.html', {'request': request, 'form': TaskForm, 'tasks':tasks})

def task_add(request):
    if request.method == "POST":
        title = request.POST.get('title').strip()
        secret_lv = request.POST.get('secret_lv')
        detail = request.POST.get('detail')
        task = Task(emp_id=request.session['id'],
            title = title,
            secret_lv = secret_lv
        )
        task.save()
        task_detail = TaskDetail(
            id = task,
            detail = detail
        )
        task_detail.save()
        return redirect("/task/add/")
    return render(request, 'task/add.html', {'request': request, 'form': TaskForm})

def task_edit(request):
    if request.method == "POST":
        task_id = request.POST.get('task_id')
        task = Task.objects.filter(id=task_id).first()
        return render(request, 'task/edit.html', {'request': request, 'task': task})
    return redirect("/task/")

def task_complete(request):
    if request.method == "POST":
        task_id = request.POST.get('task_id')
        task = Task.objects.filter(id=task_id).first()
        return render(request, 'task/complete.html', {'request': request, 'task': task})
    return redirect("/")

def do_edit(request):
    if request.method == "POST":
        task_id = request.POST.get('task_id')
        title = request.POST.get('title').strip()
        secret_lv = request.POST.get('secret_lv')
        detail = request.POST.get('detail')
        feel = request.POST.get('feel')

        task = Task.objects.filter(id=task_id).first()
        task_detail = TaskDetail.objects.filter(id=task).first()
        task.title = title
        task.secret_lv = secret_lv
        task.save()

        if feel:
            task_detail.feel = feel
        task_detail.detail = detail
        task_detail.save()
        return redirect("/task/")
    return redirect("/task/")

def do_delete(request):
    if request.method == "POST":
        task_id = request.POST.get('task_id')
        Task.objects.filter(id=task_id).delete()
        return redirect("/task/")
    return redirect("/task/")

def do_complete(request):
    if request.method == "POST":
        task_id = request.POST.get('task_id')
        feel = request.POST.get('feel')
        task = Task.objects.filter(id=task_id).first()
        task.completed = True
        task.save()
        task_detail = TaskDetail.objects.filter(id=task).first()
        task_detail.feel = feel
        task_detail.save()
    return redirect("/")