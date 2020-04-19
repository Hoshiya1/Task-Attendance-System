# Task-Attendance-System

本项目是一个使用Django开发的，整合了任务系统的考勤系统

下面是使用方法

pip install -r requirements.txt
安装所需扩展包

安装一个postgresql并为该项目创建一个数据库

在本项目的TaskAttendanceSystem\settings copy.py中找到DATABASES并配置数据库并将文件名改为setting.py，如果不知道怎么配置，自己百度“Django配置数据库”

python manage.py makemigrations
生成迁移文件（为数据库建表做准备）

python manage.py migrate
迁移数据库（开始建表）

python manage.py runserver
运行服务

python manage.py createsuperuser
创建超级管理员

进入服务器的ip地址，后面加上/admin/，进入后台管理页面，开始添加数据