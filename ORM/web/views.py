from django.http import HttpResponse, JsonResponse
from web.models import Book, Publish, Author, AuthorDetail


# ==========单表操作==========
def test1(request):
    # book = Book(title="菜鸟教程", price=300, publish="菜鸟出版社", pub_date="2008-8-8")
    # book.save()

    test = Book.objects.all().values()  # all() 查询所有内容。values() 查询部分字段的数据。
    test = Book.objects.filter(pk=2).values()  # filter() 查询符合条件的数据。pk就是主键缩写，id
    test = Book.objects.exclude(pk=2).values()  # exclude() 查询不符合条件的数据。
    # test = Book.objects.get(title="菜鸟教程").values()  # get() 查询符合条件的返回模型类的对象，且符合条件的对象只能为一个，多了或少了都会报错。
    test = Book.objects.order_by("-price").values()  # order_by() 对查询结果进行排序，"xxx"升序，"-xxx"降序。
    test = Book.objects.order_by("-price").reverse().values()  # reverse() 对查询结果进行反转。
    # test = Book.objects.count()  # count() 查询数据的数量，返回的数据是整数。
    # test = Book.objects.filter(pk=2).count()  # count() 查询数据的数量，返回的数据是整数。
    # test = Book.objects.first()  # first() 返回第一条数据，返回的数据是模型类的对象，也可以用索引下标[0]。
    # test = Book.objects.last()  # last() 返回最后一条数据，返回的数据是模型类的对象，不能用索引下标[-1]，ORM没有逆序索引。
    test = Book.objects.exists()  # exists() 判断查询的结果QuerySet列表里是否有数据。
    test = Book.objects.values("price")  # values() 查询部分字段的数据。
    test = Book.objects.values_list("price")  # values_list() 查询部分字段的数据，返回的是QuerySet类型数据，类似于list
    # ，里面不是模型类的对象，而是一个个元组，元组里放的是查询字段对应的数据。
    test = Book.objects.values_list("price").distinct()  # distinct() 对数据进行去重，返回的是QuerySet类型数据，一般是联合values
    # 或者values_list使用。

    # ==========filter() 基于双下划线的模糊查询（exclude同理），运算符号只能使用等号==========
    test = Book.objects.filter(price__in=[400, 500]).values()  # __in用于读取区间，=号后面为列表。
    test = Book.objects.filter(price__gt=400).values()  # __gt大于号 ，=号后面为数字。
    test = Book.objects.filter(price__gte=400).values()  # __gte大于等于，=号后面为数字。
    test = Book.objects.filter(price__lt=400).values()  # __lt小于，=号后面为数字。
    test = Book.objects.filter(price__lte=400).values()  # __lte小于等于，=号后面为数字。
    test = Book.objects.filter(price__range=[400, 500]).values()  # __range在左闭右闭区间之内，=号后面为两个元素的列表。
    test = Book.objects.filter(title__contains="菜").values()  # __contains包含，=号后面为字符串。
    test = Book.objects.filter(title__icontains="python").values()  # __icontains不区分大小写的包含，=号后面为字符串。
    test = Book.objects.filter(title__startswith="p").values()  # __startswith以指定字符开头，=号后面为字符串。
    test = Book.objects.filter(title__endswith="n").values()  # __endswith以指定字符结尾，=号后面为字符串。
    test = Book.objects.filter(pub_date__year=2008).values()  # __year是DateField数据类型的年份，=号后面为数字。
    test = Book.objects.filter(pub_date__month=8).values()  # __month是DateField数据类型的月份，=号后面为数字。
    test = Book.objects.filter(pub_date__day=8).values()  # __day是DateField数据类型的天数，=号后面为数字。

    # test = Book.objects.filter(title__endswith="N").delete()  # .delete() 删除。
    # test = Book.objects.filter(title__startswith="P").update(title="Java")  # .update() 修改。
    print(test, type(test))
    return HttpResponse(test)


# ==========多表操作==========
def test2(request):
    # Publish.objects.create(name="周一出版社", city="北京", email="343253855@qq.com")
    # AuthorDetail.objects.create(gender=0, tel=19850271102, addr="北京", birthday="2000-1-1")
    # Author.objects.create(name='张三', age=18, au_detail_id=3)
    # test = Publish.objects.all().values()
    # test = AuthorDetail.objects.all().values()
    # test = Author.objects.all().values()

    pass

    # # ==========添加数据；一对多==========
    # # (1) 传对象；获取出版社对象，给书籍的出版社属性 pulish 传出版社对象。
    # pub_obj = Publish.objects.filter(pk=1).first()
    # Book.objects.create(title="Django1", price=100, pub_date="2010-1-1", publish=pub_obj)
    # # (2) 传id；获取出版社对象的 id，给书籍的关联出版社字段 pulish_id 传出版社对象的 id。
    # pub_obj = Publish.objects.filter(pk=1).first()
    # pk = pub_obj.pk
    # Book.objects.create(title="Django2", price=100, pub_date="2010-1-1", publish_id=pk)
    #
    # test = Book.objects.all().values()
    # print(test, type(test))
    # return HttpResponse(test)

    pass

    # # ==========添加数据；多对多==========
    # # (1) 传对象；获取作者对象，获取书籍对象，给书籍对象的 authors 属性用 add 方法传作者对象。
    # zhang = Author.objects.filter(name="张三").first()
    # wang = Author.objects.filter(name="王五").first()
    # book = Book.objects.filter(title="Django1").first()
    # book.authors.add(zhang, wang)
    #
    # # (2) 传id；获取作者对象的 id，获取书籍对象，给书籍对象的 authors 属性用 add 方法传作者对象的 id。
    # li = Author.objects.filter(name="李四").first()
    # pk = li.pk
    # book = Book.objects.filter(title="Django2").first()
    # book.authors.add(pk)
    #
    # return HttpResponse(book)

    pass

    # # ==========关联管理器（对象调用）==========
    # # 多对多（双向均有关联管理器）；一对多（仅反向有）
    # # 正向：属性名；反向：小写类名加_set。（外键在“谁”身上，以“谁”为基的操作就是正向）
    #
    # # add()：用于多对多，把指定的模型对象添加到关联对象集（关系表）中。
    # # 注意：add()在一对多(即外键)中，只能传对象（ *QuerySet数据类型），不能传id（*[id表]）。
    # book_obj = Book.objects.get(id=2)
    # author_list = Author.objects.filter(id__gt=1)
    # book_obj.authors.add(*author_list)  # (1) *[]使用：传对象，将 id 大于1的作者对象添加到这个本书的作者集合中
    # book_obj.authors.add(*[1, 3, 5])  # (2) *[]使用：传对象id，将 id=1、id=3、id=5 的作者对象添加到这个本书的作者集合中
    #
    # li = Author.objects.filter(name="李四").first()
    # book = Book.objects.filter(title="Django3").first()
    # li.book_set.add(book)  # (3) 反向：小写表名_set，将 title="Django3" 的书对象添加到这个作者的著作集合中
    #
    # # create()：创建一个新的对象，并同时将它添加到关联对象集之中。
    # pub = Publish.objects.filter(name="周二出版社").first()
    # li = Author.objects.filter(name="李四").first()
    # book = li.book_set.create(title="Django4", price=100, pub_date="2010-1-1", publish=pub)  # 创建一个新书对象，并将其添加到这个作者的著作集合中
    # print(book, type(book))
    #
    # # remove()：从关联对象集中移除执行的模型对象。
    # # 对于 ForeignKey 对象，这个方法仅在 null = True（可以为空）时存在，无返回值。
    # author_obj = Author.objects.get(id=1)
    # book_obj = Book.objects.get(id=2)
    # author_obj.book_set.remove(book_obj)  # 将 id=2 的书对象从这个 id=1 作者的著作集合中移除
    #
    # # clear()：从关联对象集中移除一切对象，删除关联，不会删除对象。
    # # 对于 ForeignKey 对象，这个方法仅在 null = True（可以为空）时存在，无返回值。
    # book = Book.objects.filter(title="Django3").first()
    # book.authors.clear()  # 将这个本书的作者集合全部清除
    #
    # return HttpResponse("ok")

    pass

    # ==========ORM查询==========
    # 基于对象的跨表查询。
    # 正向：属性名称；反向：小写类名_set
    # (1) 一对多（外键在Book身上，以book为基的操作就是正向）
    book = Book.objects.filter(id=5).first()
    res = book.publish.city  # 获取这本书对应出版社所在的城市（正向：查询书（多）所属的出版社（一）的信息）
    print(res, type(res))
    pub = Publish.objects.filter(name="周一出版社").first()
    res = pub.book_set.all().values()  # 获取这个出版社出版的所有书（反向：查询出版社（一）所有的书（多）的信息）
    print(res, type(res))

    # (2) 一对一（外键在Author身上，以author为基的操作就是正向）
    author = Author.objects.filter(name="张三").first()
    res = author.au_detail.tel  # 查询这个作者对应的详细信息表中的信息（正向：对象.属性(author.au_detail)可以跳转到关联的表(作者详情表)）
    print(res, type(res))
    addr = AuthorDetail.objects.filter(addr="北京").first()
    res = addr.author.name  # 查询该详细信息对应的作者的信息（反向：对象.小写类名(addr.author)可以跳转到关联的表(作者表)）
    print(res, type(res))

    # (3) 多对多（外键在Book身上，以book为基的操作就是正向）
    book = Book.objects.filter(title="Django1").first()
    res = book.authors.all().values()  # 查询书的所有作者集合（正向：对象.属性(book.authors)可以跳转到关联的表(作者表)）
    print(res, type(res))
    author = Author.objects.filter(name="李四").first()
    res = author.book_set.all().values()  # 查询作者的所有书集合（反向：）
    print(res, type(res))

    # ==========基于双下划线的跨表查询==========
    # 正向：属性名称__跨表的属性名称；反向：小写类名__跨表的属性名称
    # (1) 一对多（外键在Book身上，以book为基的操作就是正向）
    res = Book.objects.filter(publish__name="周一出版社").values()  # 正向
    print(res, type(res))
    res = Publish.objects.filter(name="周一出版社").values_list("book__title", "book__price")  # 反向：通过 小写类名__跨表的属性名称（book__title，book__price） 跨表获取数据。
    print(res, type(res))

    # (2) 多对多（外键在Book身上，以book为基的操作就是正向）
    res = Book.objects.filter(authors__name="李四").values_list("title")  # 正向：通过 属性名称__跨表的属性名称(authors__name) 跨表获取数据
    print(res, type(res))
    res = Author.objects.filter(name="李四").values_list("book__title")  # 反向：通过 小写类名__跨表的属性名称（book__title） 跨表获取数据
    print(res, type(res))

    # (3) 一对一（外键在Author身上，以author为基的操作就是正向）
    res = Author.objects.filter(name="王五").values_list("au_detail__gender", "au_detail__tel")  # 正向：通过 属性名称__跨表的属性名称(au_detail__tel) 跨表获取数据
    print(res, type(res))
    res = AuthorDetail.objects.filter(author__name="王五").values_list("gender", "tel")  # 反向：通过 小写类名__跨表的属性名称（author__name） 跨表获取数据
    print(res, type(res))

    return HttpResponse("ok")


