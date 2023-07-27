from django.db import models

# ==========单表操作==========
# class Book(models.Model):
#     id = models.AutoField(primary_key=True)  # id 会自动创建，可以手动写入
#     title = models.CharField(max_length=32)  # 书籍名称
#     price = models.DecimalField(max_digits=5, decimal_places=2)  # 书籍价格
#     publish = models.CharField(max_length=32)  # 出版社名称
#     pub_date = models.DateField()  # 出版时间


# ==========多表操作==========
# 书表
class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name="书名")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="价格")
    pub_date = models.DateField(verbose_name="出版时间")
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE, verbose_name="出版社")  # 外键，多对一
    authors = models.ManyToManyField("Author", verbose_name="作者")  # 外键，多对多


# 出版社表，与书表中的书是一对多的关系；一个出版社可以出版多本书
class Publish(models.Model):
    name = models.CharField(max_length=32, verbose_name="出版社名称")
    city = models.CharField(max_length=64, verbose_name="所属城市")
    email = models.EmailField(verbose_name="邮箱")


# 作者表，与书表中的书是多对多的关系；一本书可以有多个作者，一个作者也可以有多本书
class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="作者姓名")
    age = models.SmallIntegerField(verbose_name="年龄")
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE, verbose_name="")  # 外键，一对一


# 作者详细信息表，与作者表中的作者是一一对应关系；一个作者只有一份信息
class AuthorDetail(models.Model):
    gender_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密")
    )
    gender = models.SmallIntegerField(choices=gender_choices, verbose_name="性别")
    tel = models.CharField(max_length=32, verbose_name="电话")
    addr = models.CharField(max_length=64, verbose_name="地址")
    birthday = models.DateField(verbose_name="生日")

