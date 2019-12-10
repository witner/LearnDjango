from django.db import models

# Create your models here.


#  CREATE TABLE "app_a_author" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(32) NOT NULL);
# 说明：
# 类名称（Author）：对应数据库表的名称app_a_author,注意：如果没有在类中指定表名称，默认使用应用名称+类名称作为表名称
# 类属性（name）：对应数据库表的字段， name
# 类属性方法（models.CharField(max_length=32)）：对应数据库表字段的现在类型，varchar(32)
# -----------------------------------------------------------------

class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="作者的姓名")

    def __str__(self):
        return self.name



