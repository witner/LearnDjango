from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="作者的姓名")

    def __str__(self):
        return self.name
