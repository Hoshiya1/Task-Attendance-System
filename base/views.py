from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp, Dept, Attendance
from task.models import Task, TaskDetail
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    if not request.session.get('id', None):
        return redirect("/login/")
    emp = Emp.objects.get(id=request.session['id'])
    if not request.session.get('name', None):
        name = emp.name
        dept_name = Dept.objects.filter(emp__id=emp.id).first().name
        request.session['name'] = name
        request.session['dept_name'] = dept_name
    tasks = Task.objects.filter(Q(emp_id=emp.id) & Q(completed=False)).order_by('-id')
    return render(request, 'base/index.html', {'request': request, 'tasks':tasks})

def punch(request):
    if not request.session.get('id', None):
        return redirect("/login/")
    now = datetime.now()
    time = datetime.now().__format__('%Y-%m-%d %H:%M:%S')
    atts = Attendance.objects.filter(emp__id=request.session['id']).order_by('-id')
    return render(request, 'base/punch.html', {'request': request, 'time':time, 'atts':atts})

def on_work(request):
    # 从数据库层面不允许重复打卡
    atts = Attendance.objects.filter(Q(emp_id=request.session['id']) & Q(date=datetime.now().__format__('%Y-%m-%d')))
    for att in atts:
        if att.on_work_time != None:
            return redirect("/")
    if request.method == "POST":
        now = datetime.now()
        att = Attendance(emp_id=request.session['id'],
            date = now.__format__('%Y-%m-%d'),
            on_work_time = now.__format__('%Y-%m-%d %H:%M:%S')
        )
        att.save()
        request.session['is_on_work'] = True
        return redirect("/")
    return redirect("/")

def off_work(request):
    if request.method == "POST":
        now = datetime.now()
        att = Attendance.objects.filter(Q(emp_id=request.session['id']) & Q(date=now.__format__('%Y-%m-%d'))).first()
        att.off_work_time = now.__format__('%Y-%m-%d %H:%M:%S')
        att.save()
        request.session['is_on_work'] = False
    return redirect("/")