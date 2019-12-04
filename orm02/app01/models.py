from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Author(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    sex=models.CharField(default='男',max_length=16)
    ad=models.OneToOneField(to="AuthorDetail",to_field="id",on_delete=models.CASCADE)
    # to_field="id"  可以不写,默认找主键
    # to="AuthorDetail",  to=可以不用写
    # models.SET_NULL  置空
    # on_delete=models.CASCADE  默认是级联删除,想做级联更新,直接去数据库修改表结构
    def __str__(self):
        return self.name

class AuthorDetail(models.Model):
    birthday=models.DateField()
    telephone=models.CharField(max_length=16)
    addr=models.CharField(max_length=64)


class Publish(models.Model):
    name=models.CharField(max_length=32)
    city=models.CharField(max_length=32)
    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=32)
    publishDate=models.DateField()
    # dianzan = models.IntegerField(default=100)
    # comment = models.IntegerField(default=100)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    publishs=models.ForeignKey(to="Publish",to_field="id",on_delete=models.CASCADE)
    authors=models.ManyToManyField(to='Author',)


    def get_all_authors(self):

        # authors = self.authors.all()
        # author_list = []
        # for i in authors:
        #     author_list.append(i.name)
        #
        # ret = ','.join(author_list)
        # return ret

        return ','.join([i.name for i in self.authors.all()])














