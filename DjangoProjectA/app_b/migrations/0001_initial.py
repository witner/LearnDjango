# Generated by Django 3.0 on 2019-12-10 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, verbose_name='编辑名称')),
            ],
            options={
                'db_table': 't_class',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, verbose_name='课程名称')),
            ],
            options={
                'db_table': 't_course',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, verbose_name='年级名称')),
            ],
            options={
                'db_table': 't_grade',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_id', models.ForeignKey(db_column='course_id', on_delete=django.db.models.deletion.CASCADE, to='app_b.Course', verbose_name='课程')),
            ],
            options={
                'db_table': 't_score',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, verbose_name='教师名称')),
                ('class_id', models.ManyToManyField(db_column='class_id', db_table='t_teach2cls', to='app_b.Class')),
            ],
            options={
                'db_table': 't_teacher',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, verbose_name='学生名称')),
                ('gender', models.CharField(choices=[(0, '女'), (1, '男')], max_length=4, verbose_name='性别')),
                ('class_id', models.ForeignKey(db_column='class_id', on_delete=django.db.models.deletion.CASCADE, to='app_b.Class')),
                ('course_id', models.ManyToManyField(db_column='course_id', through='app_b.Score', to='app_b.Course')),
            ],
            options={
                'db_table': 't_student',
            },
        ),
        migrations.AddField(
            model_name='score',
            name='student_id',
            field=models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, to='app_b.Student', verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_id',
            field=models.ForeignKey(db_column='teacher_id', on_delete=django.db.models.deletion.CASCADE, to='app_b.Teacher'),
        ),
        migrations.AddField(
            model_name='class',
            name='grade_id',
            field=models.ForeignKey(db_column='grade_id', on_delete=django.db.models.deletion.CASCADE, to='app_b.Grade'),
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together={('student_id', 'course_id')},
        ),
    ]
