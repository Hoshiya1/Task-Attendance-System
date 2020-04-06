from django.shortcuts import render, redirect
from .models import User


def login(request):
    if request.session.get('id', None):
        return redirect('/')
    if request.method == "POST":
        id = request.POST.get('empid').strip()
        password = request.POST.get('password').strip()
        message = '请检查填写的内容！'
        if id and password:
            # 确保id和密码都不为空或none
            try:
                user = User.objects.get(id=id)
            except:
                message = '该工号不存在！'
                return render(request, 'login/login.html', {'message': message})
            if user.password == password:
                # 验证成功
                request.session['id'] = id
                return redirect('/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', {'message':message})
        else:
            return render(request, 'login/login.html', {'message':message})

    return render(request, 'login/login.html')


# 没有登出方法，因为本项目不需要
def logout(request):
    if not request.session.get('id', None):
        return redirect("/login/")
    request.session['id'] = None
    return redirect("/login/")