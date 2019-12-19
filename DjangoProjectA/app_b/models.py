from django.db import models


# Create your models here.
class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=8, verbose_name="年级名称", unique=True)

    class Meta:
        db_table = 't_grade'

    def __str__(self):
        # 默认显示类的name字段
        return self.name

    @classmethod
    def create(cls, _name):
        if _name is 'admin':
            obj = cls(name=_name)
            return obj
        else:
            print('不合法')


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, verbose_name="教师名称")
    # class_id = models.ManyToManyField(to='Class', db_column="class_id", db_table="t_teach2cls")

    class Meta:
        db_table = 't_teacher'  # 定义表名为t_teacher

    def __str__(self):
        # 默认显示类的name字段
        return self.name


class Class(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, verbose_name="编辑名称", unique=True)
    grade_id = models.ForeignKey(to='Grade', to_field='id', on_delete=models.CASCADE, db_column="grade_id")
    teacher_id = models.ManyToManyField(to='Teacher', db_column="teacher_id", db_table="t_teach2cls")

    class Meta:
        db_table = 't_class'

    def __str__(self):
        # 默认显示类的name字段
        return self.name


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, verbose_name="学生名称")
    GENDER_CHOICES = (
        (0, u"女"),
        (1, u"男"),
    )
    gender = models.CharField(max_length=4, verbose_name="性别", choices=GENDER_CHOICES)
    class_id = models.ForeignKey(to='Class', to_field='id', on_delete=models.CASCADE, db_column="class_id")
    course_id = models.ManyToManyField(to='Course', through='Score', through_fields=('student_id', 'course_id'),
                                       db_column="course_id")

    class Meta:
        db_table = 't_student'

    def __str__(self):
        # 默认显示类的name字段
        return self.name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, verbose_name="课程名称", unique=True)
    teacher_id = models.ForeignKey(to='Teacher', to_field='id', on_delete=models.CASCADE, db_column="teacher_id")

    class Meta:
        db_table = 't_course'

    def __str__(self):
        # 默认显示类的name字段
        return self.name


class Score(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(verbose_name='学生', to="Student", to_field='id', on_delete=models.CASCADE,
                                   db_column="student_id")
    course_id = models.ForeignKey(verbose_name='课程', to="Course", to_field='id', on_delete=models.CASCADE,
                                  db_column="course_id")
    score = models.IntegerField(verbose_name="分数", default=0)

    class Meta:
        db_table = 't_score'
        unique_together = [('student_id', 'course_id'), ]

    def __str__(self):
        v = self.student_id.name + "---" + self.course_id.name
        return v
