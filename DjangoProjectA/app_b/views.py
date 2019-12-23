from django.shortcuts import render, HttpResponse
from app_b.models import *
# Create your views here.


def select(request):
    grade_queryset = Grade.objects.all()
    print(grade_queryset)
    return HttpResponse('grade_add1')




def grade_add1(request):
    # 年级添加-使用类实例对象的save方法进行添加表记录
    grade_obj1 = Grade(name="一年级")
    grade_obj1.save()
    return HttpResponse('grade_add1')


def grade_add2(request):
    # 年级添加-使用类管理器objects的create方法进行创建对象
    grade_obj2 = Grade.objects.create(name="二年级")
    return HttpResponse('grade_add2')


def grade_add3(request):
    # 年级添加，通过使用类对象自定义方法创建对象
    grade_obj3 = Grade.create('三年级')
    return HttpResponse('grade_add3')


def class_add1(request):
    # 班级添加，进行代外键数据添加操作
    grade_obj = Grade.objects.create(name="四年级")
    class_obj = Class.objects.create(name="四年级一班", grade_id=grade_obj)
    print(class_obj)
    return HttpResponse('class_add1')
