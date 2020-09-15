from django.db import models
from learn_drf import settings

# Create your models here.
class BaseModel(models.Model):
    '''基模型'''
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        '''设置为抽象的'''
        abstract = True


class Book(BaseModel):
    book_name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pic = models.ImageField(upload_to="img", default="img/1.jpg")
    publish = models.ForeignKey(to="Press", on_delete=models.CASCADE,  # 级联删除
                                db_constraint=False,  # 删除后对应的字段可以为空
                                related_name="books", )  # 反向查询的名称
    authors = models.ManyToManyField(to="Author", db_constraint=False, related_name="books")

    @property  # 类属性
    def press_name(self):
        return self.publish.press_name

    @property
    def press_address(self):
        print(self.publish,type(self.publish))
        return self.publish.address

    @property
    def author_list(self):
        return self.authors.values("author_name", "age", "detail__phone")

    @property
    def img(self):
        '''这里重写了pic，返回了一个图片的全路径'''
        return "%s%s%s" % ("http://127.0.0.1:8000/", settings.MEDIA_URL, self.pic)

    class Meta:
        db_table = "zhf_book"
        verbose_name = "图书表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name


class Press(BaseModel):
    press_name = models.CharField(max_length=128)
    pic = models.ImageField(upload_to='img', default="img/1.jpg")
    address = models.CharField(max_length=256)

    @property
    def img(self):
        '''这里重写了pic，返回了一个图片的全路径'''
        return "%s%s%s" % ("http://127.0.0.1:8000/",settings.MEDIA_URL,self.pic)

    class Meta:
        db_table = "zhf_press"
        verbose_name = "出版社"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.press_name


class Author(BaseModel):
    author_name = models.CharField(max_length=128)
    age = models.IntegerField()

    class Meta:
        db_table = "zhf_author"
        verbose_name = "作者"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.author_name


class AuthorDetail(BaseModel):
    phone = models.CharField(max_length=11)
    author = models.OneToOneField(to="Author", on_delete=models.CASCADE, related_name="detail")

    class Meta:
        db_table = "zhf_author_detail"
        verbose_name = "作者详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s的详情" % self.author.author_name
