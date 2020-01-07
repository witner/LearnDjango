from django.shortcuts import render, HttpResponse
from app_b.models import *
# Create your views here.


def select(request):
    # 过滤-主键为1的数据
    grade_queryset_001 = Grade.objects.filter(pk=1)
    print("grade_queryset_001:", grade_queryset_001)

    # 过滤字段精确匹配选项exact/iexact
    # eg：过滤name字段为六年级的
    # 过滤-精确匹配name为"六年级"、"六年级a"的数据
    grade_queryset_021 = Grade.objects.filter(name__exact="六年级")
    print("grade_queryset_021:", grade_queryset_021)
    # eg：过滤name字段为六年级a的
    grade_queryset_022 = Grade.objects.filter(name__exact="六年级a")
    print("grade_queryset_022:", grade_queryset_022)
    # eg：过滤name字段为六年级a的-不区分大小写
    grade_queryset_023 = Grade.objects.filter(name__iexact="六年级a")
    print("grade_queryset_023:", grade_queryset_023)

    # 过滤字段包含选项contains/icontains
    # eg：过滤name字段包含六年级的
    grade_queryset_031 = Grade.objects.filter(name__contains="六年级")
    print("grade_queryset_031:", grade_queryset_031)
    # eg：过滤name字段包含六年级a的-区分大小写
    grade_queryset_032 = Grade.objects.filter(name__contains="a")
    print("grade_queryset_032:", grade_queryset_032)
    # eg：过滤name字段包含六年级a的-不区分大小写
    grade_queryset_033 = Grade.objects.filter(name__icontains="a")
    print("grade_queryset_033:", grade_queryset_033)

    # 过滤字段开头结尾选项startswith/endswith/istartswith/iendswith
    # eg：过滤name字段以六开头的
    grade_queryset_041 = Grade.objects.filter(name__startswith="六")
    print("grade_queryset_041:", grade_queryset_041)
    # eg：过滤name字段以年级结尾的
    grade_queryset_042 = Grade.objects.filter(name__startswith="年级")
    print("grade_queryset_042:", grade_queryset_042)
    # eg：过滤name字段以a结尾的-区分大小写
    grade_queryset_043 = Grade.objects.filter(name__endswith="a")
    print("grade_queryset_043:", grade_queryset_043)
    # eg：过滤name字段以a结尾的-不区分大小写
    grade_queryset_044 = Grade.objects.filter(name__iendswith="a")
    print("grade_queryset_044:", grade_queryset_044)

    # 过滤字段是否为空选项isnull
    # eg: 过滤name为空的
    grade_queryset_051 = Grade.objects.filter(name__isnull=True)
    print("grade_queryset_051:", grade_queryset_051)
    # eg：过滤name不为空的
    grade_queryset_052 = Grade.objects.filter(name__isnull=False)
    print("grade_queryset_051:", grade_queryset_052)

    # 过滤字段大于、小于、大于等于、小于等于选项gt/lt/gte/lte
    # eg：过滤id字段大于4的
    grade_queryset_061 = Grade.objects.filter(id__gt=4)
    print("grade_queryset_061:", grade_queryset_061)
    # eg：过滤id字段小于4的
    grade_queryset_062 = Grade.objects.filter(id__lt=4)
    print("grade_queryset_062:", grade_queryset_062)
    # eg：过滤字段大于等于4的
    grade_queryset_063 = Grade.objects.filter(id__gte=4)
    print("grade_queryset_063:", grade_queryset_063)
    # eg：过滤字段小于等于4的
    grade_queryset_064 = Grade.objects.filter(id__lte=4)
    print("grade_queryset_064:", grade_queryset_064)

    # 过滤字段在列表中选项
    # eg：过滤id在[2,4,6,8]中的
    grade_queryset_071 = Grade.objects.filter(id__in=[2, 4, 6, 8])
    print("grade_queryset_071:", grade_queryset_071)

    # 过滤字段在范围里选项
    # eg: 过滤id在5到7之间的
    grade_queryset_081 = Grade.objects.filter(id__range=(5, 7))
    print("grade_queryset_081:", grade_queryset_081)

    # 过滤字段正则匹配
    # eg: 过滤name正则匹配年级
    grade_queryset_091 = Grade.objects.filter(name__regex=r'^.*年级.*')
    print("grade_queryset_091:", grade_queryset_091)

    return HttpResponse('select')


def select2(request):
    # 一对一的联表查询
    # 基于对象的联表查询
    # 正向查询-查询手机号为13000000001的老师名字
    teacher_detail_obj = TeacherDetail.objects.filter(telephone="13000000001").first()
    teacher_name = teacher_detail_obj.teacher_id.name
    print(teacher_name)
    # 反向查询-查询老师名为张三的手机号
    teacher_obj = Teacher.objects.filter(name="张三").first()
    telephone = teacher_obj.teacherdetail.telephone
    print(telephone)
    # 基于下划线的跨表查询
    # 正向查询-查询手机号为13000000001的老师名字
    qs = TeacherDetail.objects.filter(telephone="13000000001").values_list("teacher_id__name").first()
    print(qs)
    # 反向查询-查询老师名为张三的手机号
    qs_001 = Teacher.objects.filter(name="张三").values_list("teacherdetail__telephone").first()
    print(qs_001)





    # # 查询课程为物理课的授课老师姓名
    # course_obj = Course.objects.get(id=1)
    # print(course_obj.teacher_id.name)
    #
    # # 查询老师叫王五的授课是哪些
    # # 反向查询用对应表名+_set.all()
    # teacher_obj = Teacher.objects.filter(name="张三").first()
    # print(teacher_obj)
    # course_qs = teacher_obj.course_set.all()
    # print(course_qs)



    return HttpResponse("select2")


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
