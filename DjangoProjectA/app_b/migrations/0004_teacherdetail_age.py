# Generated by Django 3.0 on 2020-01-07 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_b', '0003_auto_20200107_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherdetail',
            name='age',
            field=models.IntegerField(default=0, verbose_name='年龄'),
        ),
    ]
