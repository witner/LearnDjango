from django.shortcuts import render, HttpResponse
from app_b.models import *
# Create your views here.


def grade_add1(request):
    # 年级添加
    grade_obj1 = Grade(name="一年级")
    grade_obj1.save()
    return HttpResponse('grade_add1')


def grade_add2(request):
    # 年级添加
    grade_obj2 = Grade.objects.create(name="二年级")
    return HttpResponse('grade_add2')


def grade_add3(request):
    # 年级添加，通过使用类对象自定义方法创建对象
    obj = Grade.create('三年级')
    return HttpResponse('grade_add3')


def grade_add4(request):
    # 年级添加，通过使用类对象自定义方法创建对象
    obj = Grade.create('三年级')
    return HttpResponse('grade_add3')





def grade_add(request):
    # 年级添加
    grade_obj1 = Grade.objects.create(name="一年级")

    grade_obj2 = Grade(name="二年级")
    grade_obj2.save()

    GRADE_LIST = ['三年级', '四年级', '五年级', '六年级']
    for grade in GRADE_LIST:
        grade_obj = Grade.objects.create(name=grade)

    return HttpResponse('grade_add')
